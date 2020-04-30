from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import (
    DATE_ESTIMATED_NA,
    POS_NEG_NOT_DONE,
    YES_NO,
    YES_NO_NA,
)
from edc_constants.constants import NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_model import models as edc_models
from edc_reportable import (
    CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    COPIES_PER_MILLILITER,
    GRAMS_PER_DECILITER,
    GRAMS_PER_LITER,
    IU_LITER,
    IU_LITER_DISPLAY,
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
)
from mapitio_lists.models import (
    DiabetesMedications,
    HypertensionMedications,
)

from ..choices import CRF_STATUS


class CrfModelMixin(BaseCrfModelMixin):
    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta(BaseCrfModelMixin.Meta):
        abstract = True


class NcdModelMixin(models.Model):

    diabetic = models.CharField(
        verbose_name=mark_safe(
            "When the patient first enrolled at the clinic, did they have <u>diabetes</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    diabetes_dx_date_known = models.CharField(
        verbose_name="Is the <u>diabetes</u> diagnosis date known?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    diabetes_dx_date = models.DateField(
        verbose_name="<u>Diabetes</u> diagnosis date", null=True, blank=True
    )

    diabetes_dx_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name="Is the <u>diabetes</u> diagnosis date estimated?",
        choices=DATE_ESTIMATED_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
    )

    diabetes_rx = models.ManyToManyField(
        DiabetesMedications, verbose_name="If YES, diabetes treatment",
    )

    other_diabetes_rx = edc_models.OtherCharField(null=True, blank=True)

    hypertensive = models.CharField(
        verbose_name=mark_safe(
            "When the patient enrolled at the clinic, did they have <u>hypertension</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    hypertension_dx_date_known = models.CharField(
        verbose_name="Is the <u>hypertension</u> diagnosis date known?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hypertension_dx_date = models.DateField(
        verbose_name="<u>Hypertension</u> diagnosis date", null=True, blank=True
    )

    hypertension_dx_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name="Is the <u>hypertension</u> diagnosis date estimated?",
        choices=DATE_ESTIMATED_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
    )

    hypertension_rx = models.ManyToManyField(
        HypertensionMedications, verbose_name="If YES, hypertension treatment",
    )

    other_hypertension_rx = edc_models.OtherCharField(null=True, blank=True)

    class Meta:
        abstract = True


class BiomedicalModelMixin(models.Model):

    drawn_date = models.DateField(
        verbose_name="Date specimen drawn", null=True, blank=True
    )

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

    serum_uric_acid = models.DecimalField(
        verbose_name="Serum uric acid levels ",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_uric_acid_units = models.CharField(
        verbose_name="Serum uric acid units",
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
        default=MILLIGRAMS_PER_DECILITER,
    )

    # AST
    ast = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="AST",
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    # AST
    alt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="ALT",
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    # ALP
    alp = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="ALP",
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    # Serum Amylase
    amylase = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="Serum Amylase",
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    # Serum GGT
    ggt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="GGT",
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    # Serum Albumin
    albumin = models.DecimalField(
        decimal_places=1,
        max_digits=6,
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="Serum Albumin",
        null=True,
        blank=True,
    )

    albumin_units = models.CharField(
        verbose_name="units",
        max_length=15,
        choices=(
            (GRAMS_PER_DECILITER, GRAMS_PER_DECILITER),
            (GRAMS_PER_LITER, GRAMS_PER_LITER),
        ),
        default=GRAMS_PER_LITER,
        null=True,
        blank=True,
    )

    # eGFR
    egfr = models.DecimalField(
        verbose_name="eGFR",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="mL/min/1.73 m2 (system calculated)",
    )

    # OTHER
    hbsag = models.CharField(
        verbose_name="HbSAg",
        max_length=15,
        choices=POS_NEG_NOT_DONE,
        null=True,
        blank=True,
    )

    hcv = models.CharField(
        verbose_name="HCV",
        max_length=15,
        choices=POS_NEG_NOT_DONE,
        null=True,
        blank=True,
    )

    # HIV
    cd4 = models.IntegerField(
        verbose_name="CD4 count",
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    )

    cd4_date = models.DateField(verbose_name="CD4 date", null=True, blank=True)

    vl = models.IntegerField(
        verbose_name="Viral load",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    vl_date = models.DateField(verbose_name="Viral load date", null=True, blank=True)

    class Meta:
        abstract = True
