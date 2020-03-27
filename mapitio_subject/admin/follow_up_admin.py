from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin import CrfModelAdminMixin


@admin.register(FollowUp, site=mapitio_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = FollowUpForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Diabetes", {"fields": ("diabetes", "diabetes_dx_date", "diabetes_rx",),},),
        (
            "Hypertension",
            {"fields": ("hypertension", "hypertension_dx_date", "hypertension_rx",),},
        ),
        (
            "Complications",
            {
                "fields": (
                    "stroke",
                    "stroke_dx_date",
                    "diabetic_foot",
                    "diabetic_foot_dx_date",
                    "chronic_heart_failure",
                    "chronic_heart_failure_dx_date",
                    "chronic_renal_failure",
                    "chronic_renal_failure_dx_date",
                ),
            },
        ),
        ("Comments", {"fields": ("crf_status", "comments",)},),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "stroke": admin.VERTICAL,
        "diabetic_foot": admin.VERTICAL,
        "chronic_heart_failure": admin.VERTICAL,
        "chronic_renal_failure": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
