from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BaselineDataForm
from ..models import BaselineData
from .modeladmin import CrfModelAdminMixin


@admin.register(BaselineData, site=mapitio_subject_admin)
class BaselineDataAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BaselineDataForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Baseline Data",
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
        "glucose_units": admin.VERTICAL,
        "glucose_fasting": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
