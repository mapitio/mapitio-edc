from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_reportable import (
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
    CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    COPIES_PER_MILLILITER,
)
from mapitio_subject.choices import CRF_STATUS

from .subject_visit import SubjectVisit


class BloodResults(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    total_cholesterol = models.DecimalField(
        verbose_name="Total Cholesterol",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    ldl = models.DecimalField(
        verbose_name="LDL",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    hdl = models.DecimalField(
        verbose_name="HDL",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    triglycerides = models.DecimalField(
        verbose_name="Triglycerides",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    serum_urea = models.DecimalField(
        verbose_name="Serum urea levels ",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_urea_units = models.CharField(
        verbose_name="Serum urea units ",
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
    )

    serum_creatinine = models.DecimalField(
        verbose_name="Serum creatinine  levels ",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_creatinine_units = models.CharField(
        verbose_name="Serum creatinine  units ",
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
    )

    cd4 = models.IntegerField(
        verbose_name="CD4 count",
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    )

    cd4_date = models.DateField(
        verbose_name="Viral load count date", null=True, blank=True
    )

    vl = models.IntegerField(
        verbose_name="Viral load",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    vl_date = models.DateField(verbose_name="Viral load date", null=True, blank=True)

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "BloodResults"
        verbose_name_plural = "BloodResults"
