from edc_model import models as edc_models

from .model_mixins import CrfModelMixin, IndicatorsModelMixin


class FollowupIndicators(IndicatorsModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    height = edc_models.HeightField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Followup Indicators"
        verbose_name_plural = "Followup Indicators"
