from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import HivHistoryForm
from ..models import HivHistory
from .modeladmin import CrfModelAdminMixin


@admin.register(HivHistory, site=mapitio_subject_admin)
class HivHistoryAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = HivHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV History",
            {
                "fields": (
                    "dx_date",
                    "initiation_date",
                    "prev_one_start_date",
                    "prev_one_end_date",
                    "prev_two_start_date",
                    "prev_two_end_date",
                    "current_regimen",
                    "previous_regimen",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    filter_horizontal = ("current_regimen",)
    radio_fields = {
        "crf_status": admin.VERTICAL,
    }
