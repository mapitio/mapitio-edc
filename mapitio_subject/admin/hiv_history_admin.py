from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import HivHistoryForm
from ..models import HivHistory
from .modeladmin import CrfModelAdminMixin

"""Previous ARV regimens"""


@admin.register(HivHistory, site=mapitio_subject_admin)
class HivHistoryAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = HivHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("HIV History", {"fields": ("dx_date", "initiation_date")}),
        ("Current ART regimen", {"fields": ("current_regimen",)},),
        (
            "Previous ART regimen (1)",
            {
                "fields": (
                    "current_is_initial",
                    "prev_one_regimen",
                    "other_prev_one_regimen",
                    "prev_one_start_date",
                    "prev_one_end_date",
                    "prev_one_switch_reason",
                ),
            },
        ),
        (
            "Previous ART regimen (2)",
            {
                "fields": (
                    "previous_is_initial",
                    "other_prev_two_regimen",
                    "prev_two_regimen",
                    "prev_two_start_date",
                    "prev_two_end_date",
                    "prev_two_switch_reason",
                ),
            },
        ),
        ("Comments", {"fields": ("crf_status", "comments",)},),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
        "current_regimen": admin.VERTICAL,
        "current_is_initial": admin.VERTICAL,
        "prev_one_regimen": admin.VERTICAL,
        "previous_is_initial": admin.VERTICAL,
        "prev_two_regimen": admin.VERTICAL,
    }
