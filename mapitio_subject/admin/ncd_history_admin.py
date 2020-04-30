from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import NcdHistoryForm
from ..models import NcdHistory


@admin.register(NcdHistory, site=mapitio_subject_admin)
class NcdHistoryAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    additional_instructions = (
        "Complete for data recorded when patient first attended the clinic "
    )

    form = NcdHistoryForm

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
        (
            "Other",
            {
                "fields": (
                    "smoking_status",
                    "takes_cholesterol_rx",
                    "cholesterol_rx",
                    "other_cholesterol_rx",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = ("diabetes_rx", "hypertension_rx", "cholesterol_rx")

    radio_fields = {
        "diabetic": admin.VERTICAL,
        "diabetes_dx_date_known": admin.VERTICAL,
        "diabetes_dx_date_estimated": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "hypertension_dx_date_known": admin.VERTICAL,
        "hypertension_dx_date_estimated": admin.VERTICAL,
        "smoking_status": admin.VERTICAL,
        "takes_cholesterol_rx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
