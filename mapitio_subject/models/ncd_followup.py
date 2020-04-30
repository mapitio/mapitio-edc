from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_model import models as edc_models

from .model_mixins import CrfModelMixin, NcdModelMixin


class NcdFollowup(CrfModelMixin, NcdModelMixin, edc_models.BaseUuidModel):

    diabetic = models.CharField(
        verbose_name=mark_safe(
            "Since the patient enrolled at this clinic, have they been diagnosed with <u>diabetes</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe(
            "Since the patient enrolled at this clinic, have they been diagnosed with <u>hypertension</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "NCD Followup"
        verbose_name_plural = "NCD Followup"
