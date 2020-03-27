from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import InvestigationsForm
from ..models import Investigations
from .modeladmin import CrfModelAdminMixin


@admin.register(Investigations, site=mapitio_subject_admin)
class InvestigationsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = InvestigationsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV History",
            {
                "fields": (
                    "chest_xray_finding_one",
                    "chest_xray_finding_two",
                    "ecg",
                    "echo",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "chest_xray_finding_one": admin.VERTICAL,
        "chest_xray_finding_two": admin.VERTICAL,
        "ecg": admin.VERTICAL,
        "echo": admin.VERTICAL,
    }
