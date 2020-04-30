from django.db import models
from edc_constants.choices import DATE_ESTIMATED_NA, YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from edc_model.validators import date_is_future
from edc_utils import get_utcnow

from ..choices import NOT_IN_CARE_REASONS
from .model_mixins import CrfModelMixin, NcdModelMixin


class FollowUp(CrfModelMixin, edc_models.BaseUuidModel):

    last_seen_date = models.DateField(
        verbose_name="Date patient last seen at this clinic",
    )

    in_care = models.CharField(
        verbose_name="Is the patient still receiving HIV care in this clinic?",
        max_length=25,
        choices=YES_NO,
    )

    reason_not_in_care = models.CharField(
        max_length=25,
        choices=NOT_IN_CARE_REASONS,
        null=True,
        blank=True,
        default=NOT_APPLICABLE,
    )

    reason_not_in_care_other = edc_models.OtherCharField(
        verbose_name="If 'Other', specify other reason not in care",
    )

    death_date = models.DateField(
        verbose_name="If 'Died', provide the date of death", null=True, blank=True,
    )

    death_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name="Is the <u>date of death</u> estimated?",
        choices=DATE_ESTIMATED_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
    )

    death_cause = models.TextField(
        verbose_name=(
            "If 'Died', enter the cause of death as recorded in the patient notes"
        ),
        null=True,
        blank=True,
    )

    has_next_appointment = models.CharField(
        verbose_name="Has the patient been scheduled for their next apointment?",
        max_length=25,
        choices=YES_NO_NA,
        null=True,
        blank=True,
        default=NOT_APPLICABLE,
    )
    next_appointment_date = models.DateField(
        verbose_name="Date of patient's next clinic appointment?",
        default=get_utcnow,
        validators=[date_is_future],
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Ups"
