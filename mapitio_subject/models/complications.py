from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NO
from edc_model import models as edc_models
from edc_model.validators import date_is_past
from edc_model.validators.date import date_is_not_now

from .model_mixins import CrfModelMixin


class Complications(CrfModelMixin, edc_models.BaseUuidModel):
    stroke = models.CharField(
        verbose_name="Stroke", max_length=25, choices=YES_NO, null=True, blank=True,
    )

    stroke_dx_date = models.DateField(
        verbose_name="If YES, date of stroke diagnosis",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
        help_text="If patient has a history of more than one stroke, report the date of the first stroke.",
    )

    diabetic_foot = models.CharField(
        verbose_name="Diabetic foot",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    diabetic_foot_dx_date = models.DateField(
        verbose_name="If YES, date of diabetic foot diagnosis",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    diabetic_retinopathy = models.CharField(
        verbose_name="Diabetic retinopathy",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    diabetic_retinopathy_dx_date = models.DateField(
        verbose_name="If YES, date of diabetic retinopathy diagnosis",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    chronic_renal_failure = models.CharField(
        verbose_name="Chronic renal failure",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    chronic_renal_failure_dx_date = models.DateField(
        verbose_name="If YES, date of chronic renal failure",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    cardiomyopathy = models.CharField(
        verbose_name="Ischaemic cardiomyopathy",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    cardiomyopathy_dx_date = models.DateField(
        verbose_name="If YES, date of ischaemic cardiomyopathy",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    peripheral_vascular = models.CharField(
        verbose_name="Peripheral vascular disease",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    peripheral_vascular_dx_date = models.DateField(
        verbose_name="If YES, date of peripheral vascular disease diagnosis",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    peripheral_neuropathy = models.CharField(
        verbose_name="Peripheral neuropathy",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    peripheral_neuropathy_dx_date = models.DateField(
        verbose_name="If YES, date of peripheral neuropathy diagnosis",
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    complications = models.CharField(
        verbose_name="Were there any other complications to report?",
        max_length=25,
        choices=YES_NO,
        default=NO,
    )

    complications_other = models.TextField(
        null=True, blank=True, help_text="Please include dates",
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Complications"
        verbose_name_plural = "Complications"
