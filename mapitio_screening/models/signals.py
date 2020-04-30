from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_consent.constants import HOSPITAL_NUMBER
from edc_constants.constants import NO
from mapitio_consent.models import SubjectConsent

from .subject_screening import SubjectScreening


def update_screening_and_consent(screening):
    options = dict(
        consent_datetime=screening.report_datetime,
        initials=screening.initials,
        gender=screening.gender,
        dob=screening.dob,
        is_dob_estimated=screening.is_dob_estimated,
        clinic_type=screening.clinic_type,
        first_name=screening.first_name,
        last_name=screening.last_name,
        identity=screening.hospital_identifier,
        confirm_identity=screening.hospital_identifier,
        identity_type=HOSPITAL_NUMBER,
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
            screening_identifier=screening.hospital_identifier
        )
    except ObjectDoesNotExist:
        SubjectConsent.objects.create(
            screening_identifier=screening.hospital_identifier, **options
        )
    else:
        for k, v in options.items():
            setattr(consent, k, v)
        consent.save_base()


@receiver(
    post_save,
    weak=False,
    dispatch_uid="update_consent_on_post_save",
    sender=SubjectScreening,
)
def update_consent_on_screening_post_save(
    sender, instance, raw, created, using, **kwargs
):
    if not raw and not kwargs.get("update_fields"):
        try:
            update_screening_and_consent(instance)
        except AttributeError as e:
            if "update_consent_on_post_save" not in str(e):
                raise AttributeError(str(e))
