from django.db import models
from django.db.models.deletion import PROTECT
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO_UNKNOWN, YES_NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from mapitio_lists.models import HypertensionTreatment
from mapitio_subject.choices import CRF_STATUS

from .subject_visit import SubjectVisit


class HypertensionReview(CrfModelMixin, edc_models.BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    dx_at_registration = models.CharField(
        verbose_name=mark_safe(
            "Did the patient have <u>hypertension</u> when they started attending the clinic?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    dx_date = models.DateField(
        verbose_name="When was the diagnosis of hypertension made?",
        null=True,
        blank=True,
    )

    dx_date_estimated = edc_models.IsDateEstimatedField()

    rx_start_date = models.DateField(
        verbose_name="When was hypertension treatment started?", null=True, blank=True,
    )

    rx_start_date_estimated = edc_models.IsDateEstimatedField()

    rx_initial = models.ForeignKey(
        HypertensionTreatment,
        on_delete=PROTECT,
        verbose_name="Initial hypertension treatment",
        related_name="hypertension_rx_registration",
        help_text="If on treatment when patient started attending the clinic, consider that as initial",
    )

    other_rx_initial = edc_models.OtherCharField(null=True, blank=True)

    rx_current = models.ForeignKey(
        HypertensionTreatment,
        on_delete=PROTECT,
        verbose_name="Current Hypertension treatment",
        related_name="Hypertension_rx_current",
    )

    other_rx_current = edc_models.OtherCharField(null=True, blank=True)

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Hypertension Review"
        verbose_name_plural = "Hypertension Review"
