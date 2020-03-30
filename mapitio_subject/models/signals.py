from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from mapitio_consent.models import SubjectConsent
from mapitio_screening.models import SubjectScreening

from .enrolment import Enrolment


def update_screening_and_consent(obj):
    try:
        screening = SubjectScreening.objects.get(
            enrolment_identifier=obj.enrolment_identifier
        )
    except ObjectDoesNotExist:
        screening = SubjectScreening.objects.create(
            enrolment_identifier=obj.enrolment_identifier,
            report_datetime=obj.clinic_registration_datetime,
            initials=obj.initials,
            gender=obj.gender,
            age_in_years=obj.age_in_years,
            clinic_type=obj.clinic_type,
            user_created=obj.user_created,
        )
    try:
        SubjectConsent.objects.get(screening_identifier=screening.screening_identifier)
    except ObjectDoesNotExist:
        SubjectConsent.objects.create(
            screening_identifier=screening.screening_identifier,
            consent_datetime=screening.report_datetime,
            initials=screening.initials,
            gender=screening.gender,
            clinic_type=screening.clinic_type,
            first_name=obj.first_name,
            last_name=obj.last_name,
            identity=obj.identity,
            confirm_identity=obj.confirm_identity,
            user_created=screening.user_created,
        )


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
        enrolment.save_base()
