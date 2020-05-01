from django.db import models
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import HOSPITAL_NOTES, NOT_APPLICABLE
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_model.models import BaseUuidModel
from edc_model.models import HistoricalRecords
from edc_reference.model_mixins import ReferenceModelMixin
from edc_sites.models import CurrentSiteManager as BaseCurrentSiteManager
from edc_sites.models import SiteModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin
from mapitio_screening.models import SubjectScreening

from ..choices import INFO_SOURCE, VISIT_REASON, VISIT_UNSCHEDULED_REASON


class CurrentSiteManager(VisitModelManager, BaseCurrentSiteManager):
    pass


class SubjectVisit(
    VisitModelMixin,
    ReferenceModelMixin,
    CreatesMetadataModelMixin,
    SiteModelMixin,
    RequiresConsentFieldsModelMixin,
    BaseUuidModel,
):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    reason = models.CharField(
        verbose_name="What is the reason for this visit report?",
        max_length=25,
        choices=VISIT_REASON,
    )

    reason_unscheduled = models.CharField(
        verbose_name="If 'unscheduled', provide reason for the unscheduled visit",
        max_length=25,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE,
    )

    info_source = models.CharField(
        verbose_name="What is the main source of this information?",
        max_length=25,
        choices=INFO_SOURCE,
        default=HOSPITAL_NOTES,
    )

    on_site = CurrentSiteManager()

    objects = VisitModelManager()

    history = HistoricalRecords()

    def __str__(self):
        return (
            f"{self.subject_identifier} {self.visit_code}.{self.visit_code_sequence} "
            f"(HMS_ID:{self.hospital_identifier})"
        )

    @property
    def hospital_identifier(self):
        return SubjectScreening.objects.get(
            subject_identifier=self.subject_identifier
        ).hospital_identifier

    class Meta(VisitModelMixin.Meta):
        pass
