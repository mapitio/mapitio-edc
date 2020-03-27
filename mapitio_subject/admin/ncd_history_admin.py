from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import NcdHistoryForm
from ..models import NcdHistory
from .modeladmin import CrfModelAdminMixin


@admin.register(NcdHistory, site=mapitio_subject_admin)
class NcdHistoryAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = NcdHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "NCD History",
            {
                "fields": (
                    "diabetes_at_enrollment",
                    "diabetes_dx_date",
                    "diabetes_rx_enrollment",
                    "hypertension_at_enrollment",
                    "hypertension_dx_date",
                    "hypertension_rx_enrollment",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "diabetes_at_enrollment": admin.VERTICAL,
        "diabetes_rx_enrollment": admin.VERTICAL,
        "hypertension_at_enrollment": admin.VERTICAL,
        "hypertension_rx_enrollment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
