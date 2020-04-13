from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BasicIndicatorsForm
from ..models import BasicIndicators
from .modeladmin import CrfModelAdminMixin


@admin.register(BasicIndicators, site=mapitio_subject_admin)
class BasicIndicatorsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BasicIndicatorsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Diagnoses",
            {
                "fields": ("hiv_pos", "diabetic", "hypertensive"),
                "description": (
                    "Indicate the diagnoses made either "
                    "before, on or after registration to this clinic"
                ),
            },
        ),
        (
            "Indicators",
            {
                "description": "Recorded when patient first started attending the clinic",
                "fields": (
                    "height",
                    "weight",
                    "waist_circumference",
                    "sys_blood_pressure",
                    "dia_blood_pressure",
                    "glucose",
                    "glucose_units",
                    "glucose_fasting",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "hiv_pos": admin.VERTICAL,
        "diabetic": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "glucose_units": admin.VERTICAL,
        "glucose_fasting": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
