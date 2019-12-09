from django.db import models
from edc_model.models.base_uuid_model import BaseUuidModel

from .subject_visit import SubjectVisit


class Baseline(BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Baseline"
        verbose_name_plural = "Baseline"
