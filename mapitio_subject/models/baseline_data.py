from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from edc_reportable import MILLIGRAMS_PER_DECILITER, MILLIMOLES_PER_LITER
from mapitio_subject.choices import CRF_STATUS, FASTING_CHOICES

from .subject_visit import SubjectVisit


class BaselineData(CrfModelMixin, edc_models.BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    height = edc_models.HeightField()

    weight = edc_models.WeightField(null=True, blank=True,)

    waist_circumference = edc_models.WaistCircumferenceField()

    sys_blood_pressure = edc_models.SystolicPressureField(null=True, blank=False,)

    dia_blood_pressure = edc_models.DiastolicPressureField(null=True, blank=False,)

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

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Baseline"
        verbose_name_plural = "Baseline"
