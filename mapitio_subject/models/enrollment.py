from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from dateutil.relativedelta import relativedelta
from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_constants.choices import GENDER
from edc_identifier.model_mixins import UniqueSubjectIdentifierModelMixin
from edc_model.models import BaseUuidModel, HistoricalRecords
from edc_model_fields.fields import IsDateEstimatedField
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils.date import get_utcnow


class Enrollment(
    UniqueSubjectIdentifierModelMixin,
    IdentityFieldsMixin,
    SiteModelMixin,
    BaseUuidModel,
):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of this report.",
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

    dob = models.DateField(verbose_name="Date of birth", null=True, blank=False)

    is_dob_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?", null=True, blank=False
    )

    gender = models.CharField(choices=GENDER, max_length=10)

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(110)],
        editable=False,
        null=True,
    )

    hospital_identifier = EncryptedCharField(unique=True, blank=False)

    clinic_registration_datetime = models.DateTimeField(
        verbose_name="Date patient enrolled at the clinic", default=get_utcnow,
    )

    on_site = CurrentSiteManager()

    objects = models.Manager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if self.dob and self.report_datetime:
            self.age_in_years = relativedelta(
                self.report_datetime, relativedelta(years=self.age_in_years)
            ).years
        else:
            self.age_in_years = None
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollment"
