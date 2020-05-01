from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from django.db import models
from django.utils.safestring import mark_safe
from django_crypto_fields.fields import EncryptedCharField
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_constants.choices import GENDER, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_model import models as edc_models
from edc_model.validators import date_is_past
from edc_model.validators.date import date_is_not_now
from edc_screening.model_mixins import (
    ScreeningFieldsModeMixin,
    ScreeningMethodsModeMixin,
)
from edc_search.model_mixins import SearchSlugModelMixin
from edc_sites.models import CurrentSiteManager, SiteModelMixin
from edc_utils import get_utcnow

from ..choices import CLINIC_CHOICES, SELECTION_METHOD
from ..constants import INTEGRATED_CLINIC
from ..eligibility import check_eligible_final


class SubjectScreeningModelError(Exception):
    pass


class SubjectScreening(
    NonUniqueSubjectIdentifierModelMixin,
    SearchSlugModelMixin,
    ScreeningMethodsModeMixin,
    ScreeningFieldsModeMixin,
    PersonalFieldsMixin,
    SiteModelMixin,
    edc_models.BaseUuidModel,
):
    screening_identifier = models.CharField(
        verbose_name="Enrollment ID",
        max_length=50,
        blank=True,
        unique=True,
        editable=False,
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

    dob = models.DateField(verbose_name="Date of birth", null=True, blank=False)

    is_dob_estimated = edc_models.IsDateEstimatedField(
        verbose_name="Is date of birth estimated?", null=True, blank=False
    )

    hospital_identifier = models.CharField(
        verbose_name="HMS Identifier",
        max_length=25,
        help_text="Hindu Mandal Hospital Identifier",
        unique=True,
    )

    confirm_hospital_identifier = models.CharField(
        verbose_name="Confirm HMS Identifier",
        max_length=25,
        help_text="Retype the Hindu Mandal Hospital Identifier",
    )

    ctc_identifier = models.CharField(
        verbose_name="CTC Identifier",
        max_length=25,
        null=True,
        blank=True,
        unique=True,
    )

    confirm_ctc_identifier = models.CharField(
        verbose_name="Confirm CTC Identifier", max_length=25, null=True, blank=True,
    )

    file_number = models.CharField(
        verbose_name="Patient File number",
        max_length=25,
        help_text=mark_safe("Patient file number from Hindu Mandal Hospital"),
        unique=True,
    )

    clinic_registration_date = models.DateField(
        verbose_name="Date patient was <u>first</u> enrolled to this clinic",
        validators=[date_is_past, date_is_not_now],
    )

    last_clinic_date = models.DateField(
        verbose_name="Date patient was <u>last</u> seen at this clinic",
        validators=[date_is_past, date_is_not_now],
        help_text="Date last seen according to information on the patient chart.",
    )

    # not used, keep for compatability
    screening_consent = models.CharField(
        verbose_name=(
            "Has the subject given his/her verbal consent "
            "to be screened for the Mapitio trial?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    # not used, keep for compatability
    selection_method = models.CharField(
        verbose_name="How was the patient selected for screening?",
        max_length=25,
        choices=SELECTION_METHOD,
        default=INTEGRATED_CLINIC,
    )

    # not used, keep for compatability
    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected",
        max_length=25,
        choices=CLINIC_CHOICES,
        default=INTEGRATED_CLINIC,
    )

    on_site = CurrentSiteManager()

    objects = models.Manager()

    def save(self, *args, **kwargs):
        """Screening Identifier is always allocated.
        """
        self.screening_identifier = self.hospital_identifier
        check_eligible_final(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollment"
        unique_together = (
            ("first_name", "dob", "initials", "last_name"),
            ("hospital_identifier", "ctc_identifier"),
        )
