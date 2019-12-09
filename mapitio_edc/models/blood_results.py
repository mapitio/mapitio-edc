from django.db import models
from edc_model.models.base_uuid_model import BaseUuidModel

from .subject_visit import SubjectVisit


class BloodResults(BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "BloodResults"
        verbose_name_plural = "BloodResults"
