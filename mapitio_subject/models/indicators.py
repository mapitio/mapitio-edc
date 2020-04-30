from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_model import models as edc_models
from edc_reportable import MILLIGRAMS_PER_DECILITER, MILLIMOLES_PER_LITER

from ..choices import FASTING_CHOICES
from .model_mixins import CrfModelMixin


class Indicators(CrfModelMixin, edc_models.BaseUuidModel):

    height = edc_models.HeightField(null=True, blank=True)

    weight = edc_models.WeightField(null=True, blank=True)

    waist_circumference = models.DecimalField(
        verbose_name="Waist circumference",
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(50.0), MaxValueValidator(175.0)],
        help_text="in centimeters",
        null=True,
        blank=True,
    )

    sys_blood_pressure = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure = edc_models.DiastolicPressureField(null=True, blank=True)

    glucose = models.DecimalField(
        verbose_name="Blood Glucose",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )

    glucose_units = models.CharField(
        verbose_name="Blood Glucose Units",
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
    )

    glucose_fasting = models.CharField(
        verbose_name="Was this a fasting or random blood glucose?",
        max_length=25,
        choices=FASTING_CHOICES,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Indicators"
        verbose_name_plural = "Indicators"
