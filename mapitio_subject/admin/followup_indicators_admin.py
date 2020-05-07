from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import FollowupIndicatorsForm
from ..models import FollowupIndicators
from .modeladmin import CrfModelAdminMixin


@admin.register(FollowupIndicators, site=mapitio_subject_admin)
class FollowupIndicatorsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    additional_instructions = mark_safe(
        "<span style='color:#ff8000'>Complete for data as of the patient's last attended clinic visit</span>"
    )

    form = FollowupIndicatorsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Indicators",
            {
                "fields": (
                    "weight",
                    "waist_circumference",
                    "sys_blood_pressure",
                    "dia_blood_pressure",
                    "glucose",
                    "glucose_units",
                    "glucose_fasting",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "glucose_units": admin.VERTICAL,
        "glucose_fasting": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
