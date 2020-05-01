from django.db import models
from edc_constants.choices import YES_NO
from edc_model import models as edc_models
from edc_model.validators import date_is_future

from ..choices import NOT_IN_CARE_REASONS
from .model_mixins import CrfModelMixin


class FollowUp(CrfModelMixin, edc_models.BaseUuidModel):

    alive = models.CharField(
        verbose_name="Is the patient known to be alive?", max_length=25, choices=YES_NO,
    )
    in_care = models.CharField(
        verbose_name="Is the patient still receiving HIV care in this clinic?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    reason_not_in_care = models.CharField(
        max_length=25, choices=NOT_IN_CARE_REASONS, null=True, blank=True,
    )

    reason_not_in_care_other = edc_models.OtherCharField(
        verbose_name="If 'Other', specify other reason not in care",
    )

    has_next_appointment = models.CharField(
        verbose_name="Has the patient been scheduled for their next apointment?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )
    next_appointment_date = models.DateField(
        verbose_name="Date of patient's next clinic appointment?",
        validators=[date_is_future],
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Ups"
