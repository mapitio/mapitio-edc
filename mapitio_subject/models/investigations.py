from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from mapitio_subject.choices import CRF_STATUS, CHEST_XRAY_CHOICES, ECG, ECHO

from .subject_visit import SubjectVisit


class Investigations(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    chest_xray_finding_one = models.CharField(
        verbose_name="Chest x-ray finding (first)",
        max_length=25,
        choices=CHEST_XRAY_CHOICES,
        help_text="Choose from findings listed (you can enter a 2nd findings below",
        null=True,
        blank=True,
    )

    chest_xray_finding_two = models.CharField(
        verbose_name="Chest x-ray finding (second)",
        max_length=25,
        choices=CHEST_XRAY_CHOICES,
        help_text="Choose from findings listed",
        null=True,
        blank=True,
    )

    ecg = models.CharField(
        verbose_name="ECG findings", max_length=25, choices=ECG, null=True, blank=True,
    )

    echo = models.CharField(
        verbose_name="ECHO findings",
        max_length=25,
        choices=ECHO,
        null=True,
        blank=True,
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Investigations"
        verbose_name_plural = "Investigations"
