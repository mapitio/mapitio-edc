from django.db import models
from edc_model import models as edc_models
from mapitio_lists.models import ChestXrayFindings, EcgFindings, EchoFindings

from .model_mixins import CrfModelMixin


class Investigations(CrfModelMixin, edc_models.BaseUuidModel):

    chest_xray_findings = models.ManyToManyField(
        ChestXrayFindings, verbose_name="Chest x-ray findings", blank=True,
    )

    chest_xray_findings_other = models.TextField(
        verbose_name="If 'Other', chest x-ray findings",
        max_length=500,
        null=True,
        blank=True,
    )

    ecg_findings = models.ManyToManyField(
        EcgFindings, verbose_name="ECG findings", blank=True,
    )

    ecg_findings_other = models.TextField(
        verbose_name="If 'Other', ECG findings", max_length=500, null=True, blank=True,
    )

    echo_findings = models.ManyToManyField(
        EchoFindings, verbose_name="ECHO findings", blank=True,
    )

    echo_findings_other = models.TextField(
        verbose_name="If 'Other', ECHO findings", max_length=500, null=True, blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Investigations"
        verbose_name_plural = "Investigations"
