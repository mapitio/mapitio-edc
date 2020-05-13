from edc_crf import CrfModelResource, NonCrfModelResource
from import_export.fields import Field

from .models import (
    BiomedicalFollowup,
    BiomedicalHistory,
    DeathReport,
    HivHistory,
    Complications,
    HivFollowup,
    Followup,
    FollowupIndicators,
    Indicators,
    Investigations,
    NcdFollowup,
    NcdHistory,
    SubjectVisit,
)


class BiomedicalFollowupResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = BiomedicalFollowup


class BiomedicalHistoryResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = BiomedicalHistory


class ComplicationsResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = Complications


class DeathReportResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = DeathReport


class FollowupResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = Followup


class FollowupIndicatorsResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = FollowupIndicators


class HivHistoryResource(CrfModelResource):
    arv_regimen_name = Field()

    def dehydrate_arv_regimen_name(self, obj):
        return obj.arv_regimen.name

    class Meta(CrfModelResource.Meta):
        model = HivHistory


class HivFollowupResource(CrfModelResource):
    arv_regimen_name = Field()

    def dehydrate_arv_regimen_name(self, obj):
        return obj.arv_regimen.name

    class Meta(CrfModelResource.Meta):
        model = HivFollowup


class IndicatorsResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = Indicators


class InvestigationsResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = Investigations


class NcdFollowupResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = NcdFollowup


class NcdHistoryResource(CrfModelResource):
    class Meta(CrfModelResource.Meta):
        model = NcdHistory


class SubjectVisitResource(NonCrfModelResource):
    class Meta(NonCrfModelResource.Meta):
        model = SubjectVisit
