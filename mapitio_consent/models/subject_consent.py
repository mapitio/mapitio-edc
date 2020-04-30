from django.apps import apps as django_apps
from django.db import models
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import GENDER
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_identifier.subject_identifier import SubjectIdentifier as BaseSubjectIdentifier
from edc_model.models import BaseUuidModel
from edc_model.models import HistoricalRecords
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_sites.models import SiteModelMixin
from edc_visit_tracking.managers import CurrentSiteManager
from mapitio_screening.choices import CLINIC_CHOICES

from ..choices import IDENTITY_TYPE
from .model_mixins import SearchSlugModelMixin


class SubjectIdentifier(BaseSubjectIdentifier):
    template = "{protocol_number}-{site_id}-{sequence}"
    padding = 4


class SubjectConsentManager(SearchSlugManager, models.Manager):
    def get_by_natural_key(self, subject_identifier, version):
        return self.get(subject_identifier=subject_identifier, version=version)


class SubjectConsent(
    ConsentModelMixin,
    SiteModelMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    NonUniqueSubjectIdentifierModelMixin,
    IdentityFieldsMixin,
    ReviewFieldsMixin,
    PersonalFieldsMixin,
    SampleCollectionFieldsMixin,
    CitizenFieldsMixin,
    VulnerabilityFieldsMixin,
    SearchSlugModelMixin,
    BaseUuidModel,
):
    """ A model completed by the user that captures the ICF.
    """

    subject_identifier_cls = SubjectIdentifier

    subject_screening_model = "mapitio_screening.subjectscreening"

    screening_identifier = models.CharField(
        verbose_name="Screening identifier",
        max_length=50,
        unique=True,
        help_text="(readonly)",
    )

    screening_datetime = models.DateTimeField(
        verbose_name="Screening datetime", null=True, editable=False
    )

    clinic_type = models.CharField(
        verbose_name="In which type of clinic was the patient screened",
        max_length=25,
        choices=CLINIC_CHOICES,
        help_text="Should match that reported on the Screening form.",
    )

    gender = models.CharField(
        verbose_name="Gender", choices=GENDER, max_length=1, null=True, blank=False,
    )

    identity_type = models.CharField(
        verbose_name="What type of identity number is this?",
        max_length=25,
        choices=IDENTITY_TYPE,
    )

    retrospective_consent = models.BooleanField(default=False)

    on_site = CurrentSiteManager()

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.subject_identifier} V{self.version}"

    def save(self, *args, **kwargs):
        subject_screening = self.get_subject_screening()
        self.screening_datetime = subject_screening.report_datetime
        self.subject_type = "subject"
        self.citizen = NOT_APPLICABLE
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_subject_screening(self):
        """Returns the subject screening model instance.

        Instance must exist since SubjectScreening is completed
        before consent.
        """
        model_cls = django_apps.get_model(self.subject_screening_model)
        return model_cls.objects.get(screening_identifier=self.screening_identifier)

    @property
    def registration_unique_field(self):
        """Required for UpdatesOrCreatesRegistrationModelMixin.
        """
        return "subject_identifier"

    class Meta(ConsentModelMixin.Meta):
        unique_together = (
            ("subject_identifier", "version"),
            ("subject_identifier", "screening_identifier"),
            ("first_name", "dob", "initials", "version"),
        )
