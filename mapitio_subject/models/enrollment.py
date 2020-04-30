from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django_crypto_fields.fields import IdentityField
from edc_consent.constants import HOSPITAL_NUMBER
from edc_consent.field_mixins import IdentityFieldsMixin, PersonalFieldsMixin
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA, YES_NO_UNKNOWN_NA
from edc_constants.constants import COMPLETE
from edc_model import models as edc_models
from edc_model.validators import date_is_future, date_is_past
from edc_screening.model_mixins import ScreeningIdentifierModelMixin
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow
from mapitio_screening.choices import CLINIC_CHOICES
from mapitio_screening.constants import INTEGRATED_CLINIC

from ..choices import CRF_STATUS, IDENTITY_TYPE


class Enrollment(
    ScreeningIdentifierModelMixin,
    IdentityFieldsMixin,
    PersonalFieldsMixin,
    SiteModelMixin,
    edc_models.BaseUuidModel,
):

    screening_identifier_field_name = "enrollment_identifier"

    enrollment_identifier = models.CharField(
        verbose_name="Enrollment ID",
        max_length=50,
        blank=True,
        unique=True,
        editable=False,
    )

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of this report.",
    )

    gender = models.CharField(
        verbose_name="Gender", choices=GENDER, max_length=1, null=True, blank=False,
    )

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(110)],
    )

    identity = IdentityField(
        verbose_name="Hospital number", help_text="Hindu Mandal Hospital Number",
    )

    identity_type = models.CharField(
        verbose_name="What type of identity number is this?",
        max_length=25,
        choices=IDENTITY_TYPE,
        default=HOSPITAL_NUMBER,
        editable=False,
    )

    confirm_identity = IdentityField(
        verbose_name="Confirm Hindu Mandal Hospital Number",
        null=True,
        blank=False,
        help_text="Retype the Hindu Mandal Hospital Number",
    )

    ctc_identifier = IdentityField(verbose_name="CTC Identifier")

    confirm_ctc_identifier = IdentityField(verbose_name="Confirm CTC Identifier")

    clinic_registration_date = models.DateField(
        verbose_name="Date patient was first enrolled to this clinic",
        validators=[date_is_past],
    )

    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected",
        max_length=25,
        choices=CLINIC_CHOICES,
        default=INTEGRATED_CLINIC,
        editable=False,
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS, default=COMPLETE,
    )

    comments = models.TextField(null=True, blank=True)

    on_site = CurrentSiteManager()

    objects = models.Manager()

    history = edc_models.HistoricalRecords()

    def __str__(self):
        return f"{self.first_name} {self.initials}"

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollment"
