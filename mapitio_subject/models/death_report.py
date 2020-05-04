from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import DATE_ESTIMATED, YES_NO
from edc_constants.constants import NO
from edc_model import models as edc_models
from edc_model.validators import date_is_past

from .model_mixins import CrfModelMixin


class DeathReport(CrfModelMixin, edc_models.BaseUuidModel):

    death_date = models.DateField(
        verbose_name="Date of death", validators=[date_is_past],
    )

    death_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name="Is the date of death estimated?", choices=DATE_ESTIMATED,
    )

    death_cause_known = models.CharField(
        verbose_name=mark_safe("Is the cause of death known?"),
        max_length=15,
        choices=YES_NO,
        default=NO,
    )

    death_cause = models.TextField(
        verbose_name="The cause of death as recorded in the patient notes",
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Death Report"
        verbose_name_plural = "Death Reports"
