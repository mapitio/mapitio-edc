from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import HivHistoryForm
from ..models import HivHistory


@admin.register(HivHistory, site=mapitio_subject_admin)
class HivHistoryAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    additional_instructions = (
        "Complete for data recorded when patient first attended the clinic "
    )

    form = HivHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV",
            {
                "fields": (
                    "hiv_pos_date",
                    "arv_initiation_date",
                    "arv_regimen",
                    "arv_regimen_other",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "arv_regimen": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
