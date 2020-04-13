from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.deletion import PROTECT
from edc_constants.choices import YES_NO_NA, YES_NO
from edc_constants.constants import NOT_APPLICABLE, NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from mapitio_lists.models import ArvRegimens
from mapitio_subject.choices import CRF_STATUS


from .subject_visit import SubjectVisit


class HivReview(CrfModelMixin, edc_models.BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    dx_date = models.DateField(
        verbose_name="When did the patient first test positive for HIV",
        null=True,
        blank=True,
    )

    initiation_date = models.DateField(
        verbose_name="Date antiretroviral therapy commenced", null=True, blank=True
    )

    current_regimen = models.ForeignKey(
        ArvRegimens,
        on_delete=PROTECT,
        related_name="current_regimen",
        null=True,
        blank=False,
    )

    other_current_regimen = edc_models.OtherCharField(null=True, blank=True)

    current_is_initial = models.CharField(
        verbose_name="Is the <u>current</u> regimen the patient's initial regimen?",
        max_length=5,
        choices=YES_NO,
        default=NO,
    )

    prev_one_regimen = models.ForeignKey(
        ArvRegimens,
        on_delete=PROTECT,
        verbose_name=mark_safe(
            "What was the ART regimen <u>immediately before</u> the current regimen"
        ),
        related_name="prev_one_regimen",
        help_text="This is 'previous' regimen",
        null=True,
        blank=False,
    )

    other_prev_one_regimen = edc_models.OtherCharField(null=True, blank=True)

    prev_one_start_date = models.DateField(
        verbose_name="Date commenced", null=True, blank=True
    )

    prev_one_end_date = models.DateField(
        verbose_name="Date ended", null=True, blank=True
    )

    prev_one_switch_reason = models.CharField(
        verbose_name="Reason for switching", max_length=25, null=True, blank=True
    )

    previous_is_initial = models.CharField(
        verbose_name=mark_safe(
            "Was the 'previous' regimen listed above the patient's <u>initial</u> regimen?"
        ),
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If NO, provide details below.",
    )

    prev_two_regimen = models.ForeignKey(
        ArvRegimens,
        on_delete=PROTECT,
        verbose_name=mark_safe(
            "What was the ART regimen <u>before</u> the 'previous' regimen listed above?"
        ),
        related_name="prev_two_regimen",
        null=True,
        blank=False,
    )

    other_prev_two_regimen = edc_models.OtherCharField(null=True, blank=True)

    prev_two_start_date = models.DateField(
        verbose_name="Date commenced", null=True, blank=True
    )

    prev_two_end_date = models.DateField(
        verbose_name="Date ended", null=True, blank=True
    )

    prev_two_switch_reason = models.CharField(
        verbose_name="Reason for switching", max_length=25, null=True, blank=True
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "HIV Review"
        verbose_name_plural = "HIV Review"
