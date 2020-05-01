from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import ComplicationsForm
from ..models import Complications
from .fieldsets import comment_fieldset_tuple
from .modeladmin import CrfModelAdminMixin


@admin.register(Complications, site=mapitio_subject_admin)
class ComplicationsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = ComplicationsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Complications",
            {
                "fields": (
                    "stroke",
                    "stroke_dx_date",
                    "diabetic_foot",
                    "diabetic_foot_dx_date",
                    "cardiomyopathy",
                    "cardiomyopathy_dx_date",
                    "chronic_renal_failure",
                    "chronic_renal_failure_dx_date",
                    "diabetic_retinopathy",
                    "diabetic_retinopathy_dx_date",
                    "peripheral_vascular",
                    "peripheral_vascular_dx_date",
                    "peripheral_neuropathy",
                    "peripheral_neuropathy_dx_date",
                    "complications",
                    "complications_other",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "stroke": admin.VERTICAL,
        "diabetic_foot": admin.VERTICAL,
        "cardiomyopathy": admin.VERTICAL,
        "diabetic_retinopathy": admin.VERTICAL,
        "peripheral_vascular": admin.VERTICAL,
        "peripheral_neuropathy": admin.VERTICAL,
        "chronic_renal_failure": admin.VERTICAL,
        "complications": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
