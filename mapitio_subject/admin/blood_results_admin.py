from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BloodResultsForm
from ..models import BloodResults
from .modeladmin import CrfModelAdminMixin


@admin.register(BloodResults, site=mapitio_subject_admin)
class BloodResultsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BloodResultsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Blood Results",
            {
                "fields": (
                    "total_cholesterol",
                    "ldl",
                    "hdl",
                    "triglycerides",
                    "serum_urea",
                    "serum_urea_units",
                    "serum_creatinine",
                    "serum_creatinine_units",
                    "cd4",
                    "cd4_date",
                    "vl",
                    "vl_date",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "serum_urea_units": admin.VERTICAL,
        "serum_creatinine_units": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
