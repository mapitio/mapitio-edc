from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from edc_constants.choices import YES_NO
from edc_model.models import BaseUuidModel
from edc_screening.model_mixins import ScreeningModelMixin
from edc_screening.screening_identifier import ScreeningIdentifier
from mapitio_screening.constants import INTEGRATED_CLINIC

from ..choices import CLINIC_CHOICES, SELECTION_METHOD


class SubjectScreeningModelError(Exception):
    pass


class ScreeningIdentifier(ScreeningIdentifier):
    template = "S{random_string}"


class SubjectScreening(
    ScreeningModelMixin, BaseUuidModel,
):
    identifier_cls = ScreeningIdentifier

    enrolment_identifier = models.CharField(
        verbose_name="Enrolment ID",
        max_length=50,
        blank=True,
        unique=True,
        editable=False,
    )

    screening_consent = models.CharField(
        verbose_name=(
            "Has the subject given his/her verbal consent "
            "to be screened for the INTE Africa trial?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    selection_method = models.CharField(
        verbose_name="How was the patient selected for screening?",
        max_length=25,
        choices=SELECTION_METHOD,
        default=INTEGRATED_CLINIC,
    )

    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected",
        max_length=25,
        choices=CLINIC_CHOICES,
        default=INTEGRATED_CLINIC,
    )

    initials = EncryptedCharField(
        validators=[
            RegexValidator("[A-Z]{1,3}", "Invalid format"),
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ],
        help_text="Use UPPERCASE letters only. May be 2 or 3 letters.",
        blank=False,
    )

    class Meta:
        verbose_name = "Subject Screening"
        verbose_name_plural = "Subject Screening"
