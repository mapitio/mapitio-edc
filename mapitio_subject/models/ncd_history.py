from django.db import models
from edc_constants.choices import YES_NO_UNKNOWN
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from mapitio_subject.choices import CRF_STATUS

from .subject_visit import SubjectVisit


class NcdHistory(CrfModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    diabetes_at_enrollment = models.CharField(
        verbose_name="Did the patient have Diabetes when they started attending the clinic?",
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    diabetes_dx_date = models.DateField(
        verbose_name="If YES, when was the diagnosis of diabetes made?",
        null=True,
        blank=True,
    )

    diabetes_rx_enrollment = models.TextField(
        verbose_name="List of diabetes treatment when patient started attending the clinic",
        null=True,
        blank=True,
    )

    hypertension_at_enrollment = models.CharField(
        verbose_name="Did the patient have Hypertension when they started attending the clinic",
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    hypertension_dx_date = models.DateField(
        verbose_name="If YES, when was the diagnosis of hypertension made?",
        null=True,
        blank=True,
    )

    hypertension_rx_enrollment = models.TextField(
        verbose_name="List of hypertension treatment when patient started attending the clinic",
        null=True,
        blank=True,
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "NCD History"
        verbose_name_plural = "NCD History"
