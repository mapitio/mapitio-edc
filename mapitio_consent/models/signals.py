from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from edc_randomization.site_randomizers import site_randomizers
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from mapitio_screening.models import SubjectScreening
from mapitio_subject.models import SubjectVisit

from .subject_consent import SubjectConsent


class MapitioSubjectConsentError(Exception):
    pass


@receiver(
    post_save,
    weak=False,
    sender=SubjectConsent,
    dispatch_uid="subject_consent_on_post_save",
)
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this consented subject, if
    it does not exist.
    """
    if not raw:
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                "mapitio_prn.onschedule"
            )
            try:
                schedule.refresh_schedule(
                    subject_identifier=instance.subject_identifier
                )
            except ObjectDoesNotExist as e:
                raise MapitioSubjectConsentError(
                    f"Is subject on schedule? See `{instance.subject_identifier}`. Got `{e}`"
                )
        else:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier
            )

            if subject_screening.clinic_type != instance.clinic_type:
                raise MapitioSubjectConsentError(
                    f"Clinic type reported on screening does not match consent."
                    f"Expected {subject_screening.clinic_type}. Got {instance.clinic_type}"
                )
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(
                update_fields=["subject_identifier", "consented"]
            )

            # randomize
            # TODO: should get randomizer name "default" from model or Consent object
            site_randomizers.randomize(
                "default",
                subject_identifier=instance.subject_identifier,
                report_datetime=instance.consent_datetime,
                site=instance.site,
                user=instance.user_created,
            )

            # put subject on primary schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                "mapitio_prn.onschedule"
            )
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime,
            )


@receiver(
    post_delete,
    weak=False,
    sender=SubjectConsent,
    dispatch_uid="subject_consent_on_post_delete",
)
def subject_consent_on_post_delete(sender, instance, using, **kwargs):
    """Updates/Resets subject screening.
    """
    # don't allow if subject visits exist. This should be caught
    # in the ModelAdmin delete view
    if SubjectVisit.objects.filter(
        subject_identifier=instance.subject_identifier
    ).exists():
        raise ValidationError("Unable to delete consent. Visit data exists.")

    _, schedule = site_visit_schedules.get_by_onschedule_model("mapitio_prn.onschedule")
    schedule.take_off_schedule(
        subject_identifier=instance.subject_identifier,
        offschedule_datetime=instance.consent_datetime,
    )

    # update subject screening
    subject_screening = SubjectScreening.objects.get(
        screening_identifier=instance.screening_identifier
    )
    subject_screening.consented = False
    subject_screening.subject_identifier = subject_screening.subject_screening_as_pk
    subject_screening.save()
