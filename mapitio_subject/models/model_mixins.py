from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import (
    DATE_ESTIMATED_NA,
    POS_NEG_NOT_DONE,
    YES_NO,
    YES_NO_NA,
)
from edc_constants.constants import INCOMPLETE, NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_model import models as edc_models
from edc_model.validators import date_is_past
from edc_model.validators.date import date_is_not_now
from edc_reportable import (
    CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    COPIES_PER_MILLILITER,
    GRAMS_PER_DECILITER,
    GRAMS_PER_LITER,
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
        verbose_name="CRF status",
        max_length=25,
        choices=CRF_STATUS,
        default=INCOMPLETE,
        help_text="If some data is still pending, flag this CRF as incomplete",
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
        verbose_name=mark_safe("Is the <u>diabetes</u> diagnosis date known?"),
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    diabetes_dx_date = models.DateField(
        verbose_name=mark_safe("<u>Diabetes</u> diagnosis date"), null=True, blank=True
    )

    diabetes_dx_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name=mark_safe("Is the <u>diabetes</u> diagnosis date estimated?"),
        choices=DATE_ESTIMATED_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
    )

    diabetes_rx = models.ManyToManyField(
        DiabetesMedications, verbose_name="Diabetes treatment",
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
        verbose_name=mark_safe("Is the <u>hypertension</u> diagnosis date known?"),
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hypertension_dx_date = models.DateField(
        verbose_name=mark_safe("<u>Hypertension</u> diagnosis date"),
        null=True,
        blank=True,
    )

    hypertension_dx_date_estimated = edc_models.IsDateEstimatedField(
        verbose_name=mark_safe("Is the <u>hypertension</u> diagnosis date estimated?"),
        choices=DATE_ESTIMATED_NA,
        null=True,
        blank=False,
        default=NOT_APPLICABLE,
    )

    hypertension_rx = models.ManyToManyField(
        HypertensionMedications, verbose_name="Hypertension treatment",
    )

    other_hypertension_rx = edc_models.OtherCharField(null=True, blank=True)

    class Meta:
        abstract = True


class BiomedicalModelMixin(models.Model):

    total_cholesterol = models.DecimalField(
        verbose_name=mark_safe("<u>Total cholesterol</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    total_cholesterol_date = models.DateField(
        verbose_name=mark_safe("<i>Total cholesterol date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    ldl = models.DecimalField(
        verbose_name=mark_safe("<u>LDL</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    ldl_date = models.DateField(
        verbose_name=mark_safe("<i>LDL date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    hdl = models.DecimalField(
        verbose_name=mark_safe("<u>HDL</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    hdl_date = models.DateField(
        verbose_name=mark_safe("<i>HDL date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    triglycerides = models.DecimalField(
        verbose_name=mark_safe("<u>Triglycerides</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="mmol/L",
    )

    triglycerides_date = models.DateField(
        verbose_name=mark_safe("<i>Triglycerides date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    serum_urea = models.DecimalField(
        verbose_name=mark_safe("<u>Serum urea</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_urea_units = models.CharField(
        verbose_name=mark_safe("<i>Serum urea units</i>"),
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
    )

    serum_urea_date = models.DateField(
        verbose_name=mark_safe("<i>Serum urea date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    serum_creatinine = models.DecimalField(
        verbose_name=mark_safe("<u>Serum creatinine</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_creatinine_units = models.CharField(
        verbose_name=mark_safe("<i>Serum creatinine units</i>"),
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
    )

    serum_creatinine_date = models.DateField(
        verbose_name=mark_safe("<i>Serum creatinine date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    serum_uric_acid = models.DecimalField(
        verbose_name=mark_safe("<u>Serum uric acid</u>"),
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    serum_uric_acid_units = models.CharField(
        verbose_name=mark_safe("<i>Serum uric acid units</i>"),
        max_length=15,
        choices=(
            (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
            (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
        ),
        null=True,
        blank=True,
        default=MILLIGRAMS_PER_DECILITER,
    )

    serum_uric_acid_date = models.DateField(
        verbose_name=mark_safe("<i>Serum uric acid date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # AST
    ast = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>AST</u>"),
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    ast_date = models.DateField(
        verbose_name=mark_safe("<i>AST date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # AST
    alt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>ALT</u>"),
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    alt_date = models.DateField(
        verbose_name=mark_safe("<i>ALT date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # ALP
    alp = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>ALP</u>"),
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    alp_date = models.DateField(
        verbose_name=mark_safe("<i>ALP date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # Serum Amylase
    amylase = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>Serum Amylase</u>"),
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    amylase_date = models.DateField(
        verbose_name=mark_safe("<i>Serum Amylase date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # Serum GGT
    ggt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>GGT</u>"),
        null=True,
        blank=True,
        help_text=IU_LITER_DISPLAY,
    )

    ggt_date = models.DateField(
        verbose_name=mark_safe("<i>GGT date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # Serum Albumin
    albumin = models.DecimalField(
        decimal_places=1,
        max_digits=6,
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name=mark_safe("<u>Serum Albumin</u>"),
        null=True,
        blank=True,
    )

    albumin_units = models.CharField(
        verbose_name=mark_safe("<i>Serum Albumin units</i>"),
        max_length=15,
        choices=(
            (GRAMS_PER_DECILITER, GRAMS_PER_DECILITER),
            (GRAMS_PER_LITER, GRAMS_PER_LITER),
        ),
        default=GRAMS_PER_LITER,
        null=True,
        blank=True,
    )

    albumin_date = models.DateField(
        verbose_name=mark_safe("<i>Serum Albumin date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # eGFR
    egfr = models.DecimalField(
        verbose_name=mark_safe("<u>eGFR</u>"),
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
        help_text="mL/min/1.73 m2 (system calculated)",
    )

    # OTHER
    hbsag = models.CharField(
        verbose_name=mark_safe("<u>HbSAg</u>"),
        max_length=15,
        choices=POS_NEG_NOT_DONE,
        null=True,
        blank=True,
    )

    hbsag_date = models.DateField(
        verbose_name=mark_safe("<i>HbSAg date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    hcv = models.CharField(
        verbose_name=mark_safe("<u>HCV</u>"),
        max_length=15,
        choices=POS_NEG_NOT_DONE,
        null=True,
        blank=True,
    )

    hcv_date = models.DateField(
        verbose_name=mark_safe("<i>HCV date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    # HIV
    cd4 = models.IntegerField(
        verbose_name=mark_safe("<u>CD4 count</u>"),
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    )

    cd4_date = models.DateField(
        verbose_name=mark_safe("<i>CD4 date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    vl = models.IntegerField(
        verbose_name=mark_safe("<u>Viral load</u>"),
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    vl_date = models.DateField(
        verbose_name=mark_safe("<i>Viral load date</i>"),
        validators=[date_is_past, date_is_not_now],
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
