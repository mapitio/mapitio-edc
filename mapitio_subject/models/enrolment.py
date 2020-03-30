from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from dateutil.relativedelta import relativedelta
from django.db import models
from edc_consent.constants import HOSPITAL_NUMBER
from edc_consent.field_mixins import IdentityFieldsMixin, PersonalFieldsMixin
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_screening.model_mixins import ScreeningIdentifierModelMixin
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils import age
from edc_utils.date import get_utcnow
from mapitio_screening.choices import CLINIC_CHOICES
from mapitio_screening.constants import INTEGRATED_CLINIC

from ..choices import CRF_STATUS, IDENTITY_TYPE


class Enrolment(
    ScreeningIdentifierModelMixin,
    IdentityFieldsMixin,
    PersonalFieldsMixin,
    SiteModelMixin,
    BaseUuidModel,
):

    screening_identifier_field_name = "enrolment_identifier"

    enrolment_identifier = models.CharField(
        verbose_name="Enrolment ID",
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

    identity_type = models.CharField(
        verbose_name="What type of identity number is this?",
        max_length=25,
        choices=IDENTITY_TYPE,
        default=HOSPITAL_NUMBER,
    )

    clinic_registration_datetime = models.DateTimeField(
        verbose_name="Date patient enrolled at the clinic", default=get_utcnow,
    )

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(110)],
        editable=False,
        null=True,
    )

    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected",
        max_length=25,
        choices=CLINIC_CHOICES,
        default=INTEGRATED_CLINIC,
        editable=False,
    )

    crf_status = models.CharField(
        verbose_name="CRF status", max_length=25, choices=CRF_STATUS
    )

    comments = models.TextField(null=True, blank=True)

    on_site = CurrentSiteManager()

    objects = models.Manager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.first_name} {self.initials}"

    def save(self, *args, **kwargs):
        if self.age_in_years:
            if self.dob and self.report_datetime:
                self.age_in_years = relativedelta(
                    self.report_datetime.date(), relativedelta(years=self.age_in_years)
                ).years
        else:
            self.age_in_years = age(self.dob, self.report_datetime.date()).years
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Enrolment"
        verbose_name_plural = "Enrolment"
