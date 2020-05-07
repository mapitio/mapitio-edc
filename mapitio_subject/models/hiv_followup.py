from django.db import models
from django.db.models.deletion import PROTECT
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_model import models as edc_models
from mapitio_lists.models import ArvRegimens

from .model_mixins import CrfModelMixin, NcdModelMixin


class HivFollowup(CrfModelMixin, NcdModelMixin, edc_models.BaseUuidModel):
    arv_modification = models.CharField(
        verbose_name="Have there been any modifications to the patient's ARV regimen since enrollment?",
        max_length=25,
        choices=YES_NO,
    )

    arv_modification_date = models.DateField(
        verbose_name=mark_safe("Most <u>recent</u> date ARV regimen changed"),
        null=True,
        blank=True,
    )

    arv_regimen = models.ForeignKey(
        ArvRegimens,
        verbose_name="Most recent ARV Regimen",
        on_delete=PROTECT,
        null=True,
        blank=False,
    )

    arv_regimen_other = edc_models.OtherCharField(null=True, blank=True)

    dtg_switched = models.CharField(
        verbose_name="Has the patient ever been switched to a DTG-based regimen?",
        max_length=25,
        choices=YES_NO,
    )

    dtg_switched_date = models.DateField(
        verbose_name="Date patient initiated on or switched to a DTG-base regimen",
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "HIV Followup"
        verbose_name_plural = "HIV Followup"
