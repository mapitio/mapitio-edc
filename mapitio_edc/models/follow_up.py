from django.db import models
from edc_model.models.base_uuid_model import BaseUuidModel

from .subject_visit import SubjectVisit


class FollowUp(BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Ups"
