from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from mapitio_lists.models import ArvRegimens
from mapitio_subject.choices import CRF_STATUS

from .subject_visit import SubjectVisit


class HivHistory(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    dx_date = models.DateField(
        verbose_name="When was the diagnosis made", null=True, blank=True
    )

    initiation_date = models.DateField(
        verbose_name="Date antiretroviral therapy commenced", null=True, blank=True
    )

    current_regimen = models.ManyToManyField(
        ArvRegimens, related_name="current_regimen"
    )

    previous_regimen = models.ManyToManyField(
        ArvRegimens, related_name="previous_regimen"
    )

    prev_one_start_date = models.DateField(
        verbose_name="Date commenced", null=True, blank=True
    )

    prev_one_end_date = models.DateField(
        verbose_name="Date ended", null=True, blank=True
    )

    prev_one_end_date = models.CharField(
        verbose_name="Reason for switching", max_length=25, null=True, blank=True
    )

    prev_two_start_date = models.DateField(
        verbose_name="Date commenced", null=True, blank=True
    )

    prev_two_end_date = models.DateField(
        verbose_name="Date ended", null=True, blank=True
    )

    prev_two_end_date = models.CharField(
        verbose_name="Reason for switching", max_length=25, null=True, blank=True
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "HIV History"
        verbose_name_plural = "HIV History"
