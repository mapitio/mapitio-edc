from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_constants.constants import NO, YES
from mapitio_consent.models import SubjectConsent
from mapitio_screening.models import SubjectScreening

from .enrolment import Enrolment


def update_screening_and_consent(enrolment):
    try:
        screening = SubjectScreening.objects.get(
            enrolment_identifier=enrolment.enrolment_identifier
        )
    except ObjectDoesNotExist:
        screening = SubjectScreening.objects.create(
            enrolment_identifier=enrolment.enrolment_identifier,
            report_datetime=enrolment.clinic_registration_datetime,
            initials=enrolment.initials,
            gender=enrolment.gender,
            age_in_years=enrolment.age_in_years,
            clinic_type=enrolment.clinic_type,
            user_created=enrolment.user_created,
        )
    options = dict(
        consent_datetime=screening.report_datetime,
        initials=screening.initials,
        gender=screening.gender,
        dob=enrolment.dob,
        is_dob_estimated=enrolment.is_dob_estimated,
        clinic_type=screening.clinic_type,
        first_name=enrolment.first_name,
        last_name=enrolment.last_name,
        identity=enrolment.identity,
        confirm_identity=enrolment.confirm_identity,
        identity_type=enrolment.identity_type,
        user_created=screening.user_created,
        is_incarcerated=NO,
        consent_reviewed=NO,
        study_questions=NO,
        assessment_score=NO,
        consent_signature=NO,
        consent_copy=NO,
    )
    try:
        consent = SubjectConsent.objects.get(
            screening_identifier=screening.screening_identifier
        )
    except ObjectDoesNotExist:
        SubjectConsent.objects.create(
            screening_identifier=screening.screening_identifier, **options
        )
    else:
        for k, v in options.items():
            setattr(consent, k, v)
        consent.save_base()


@receiver(
    post_save, weak=False, dispatch_uid="update_consent_on_post_save", sender=Enrolment,
)
def update_consent_on_enrolment_post_save(
    sender, instance, raw, created, using, **kwargs
):
    if not raw and not kwargs.get("update_fields"):
        try:
            update_screening_and_consent(instance)
        except AttributeError as e:
            if "update_consent_on_post_save" not in str(e):
                raise AttributeError(str(e))


@receiver(
    post_save,
    weak=False,
    dispatch_uid="update_enrolment_consent_post_save",
    sender=SubjectConsent,
)
def update_enrolment_consent_post_save(sender, instance, raw, created, using, **kwargs):
    if not raw and not kwargs.get("update_fields"):
        screening = SubjectScreening.objects.get(
            screening_identifier=instance.screening_identifier
        )
        enrolment = Enrolment.objects.get(
            enrolment_identifier=screening.enrolment_identifier
        )
        enrolment.subject_identifier = instance.subject_identifier
        enrolment.save(update_fields=["subject_identifier"])
