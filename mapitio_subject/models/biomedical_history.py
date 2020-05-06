from edc_model import models as edc_models

from .model_mixins import BiomedicalModelMixin, CrfModelMixin


class BiomedicalHistory(BiomedicalModelMixin, CrfModelMixin, edc_models.BaseUuidModel):
    class Meta(CrfModelMixin.Meta):
        verbose_name = "Biomedical History"
        verbose_name_plural = "Biomedical History"
