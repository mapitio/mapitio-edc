from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, SMOKER_STATUS
from edc_model import models as edc_models
from mapitio_lists.models import CholesterolMedications

from .model_mixins import CrfModelMixin, NcdModelMixin


class NcdHistory(CrfModelMixin, NcdModelMixin, edc_models.BaseUuidModel):

    diabetic = models.CharField(
        verbose_name=mark_safe(
            "When the patient first enrolled at the clinic, did they have <u>diabetes</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe(
            "When the patient enrolled at the clinic, did they have <u>hypertension</u>?"
        ),
        max_length=25,
        choices=YES_NO,
    )

    smoking_status = models.CharField(
        verbose_name="Smoker? Which best describes the patient:",
        max_length=15,
        choices=SMOKER_STATUS,
    )

    takes_cholesterol_rx = models.CharField(
        verbose_name=(
            "Is the patient currently taking any statins or other medications "
            "for control of blood cholesterol?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    cholesterol_rx = models.ManyToManyField(
        CholesterolMedications, verbose_name="If YES, blood cholesterol medications",
    )

    other_cholesterol_rx = edc_models.OtherCharField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "NCD History"
        verbose_name_plural = "NCD History"
