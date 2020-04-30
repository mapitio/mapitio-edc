from django.db import models
from django.db.models.deletion import PROTECT
from edc_model import models as edc_models
from mapitio_lists.models import ArvRegimens

from .model_mixins import CrfModelMixin, NcdModelMixin


class HivHistory(CrfModelMixin, NcdModelMixin, edc_models.BaseUuidModel):
    hiv_pos_date = models.DateField(
        verbose_name="When did the patient first test positive for HIV",
        null=True,
        blank=True,
    )

    arv_initiation_date = models.DateField(
        verbose_name="Date antiretroviral therapy commenced", null=True, blank=True
    )

    arv_regimen = models.ForeignKey(
        ArvRegimens,
        verbose_name="ARV Regimen at enrollment",
        on_delete=PROTECT,
        null=True,
        blank=False,
    )

    arv_regimen_other = edc_models.OtherCharField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "HIV History"
        verbose_name_plural = "HIV History"
