from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import NcdFollowupForm
from ..models import NcdFollowup


@admin.register(NcdFollowup, site=mapitio_subject_admin)
class NcdFollowupAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    form = NcdFollowupForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diabetes",
            {
                "fields": (
                    "diabetic",
                    "diabetes_dx_date_known",
                    "diabetes_dx_date",
                    "diabetes_dx_date_estimated",
                    "diabetes_rx",
                    "other_diabetes_rx",
                ),
            },
        ),
        (
            "Hypertension",
            {
                "fields": (
                    "hypertensive",
                    "hypertension_dx_date_known",
                    "hypertension_dx_date",
                    "hypertension_dx_date_estimated",
                    "hypertension_rx",
                    "other_hypertension_rx",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = ("diabetes_rx", "hypertension_rx")

    radio_fields = {
        "diabetic": admin.VERTICAL,
        "diabetes_dx_date_known": admin.VERTICAL,
        "diabetes_dx_date_estimated": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "hypertension_dx_date_known": admin.VERTICAL,
        "hypertension_dx_date_estimated": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
