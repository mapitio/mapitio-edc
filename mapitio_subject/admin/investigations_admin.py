from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

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
            "Chest X-ray",
            {"fields": ("chest_xray_findings", "chest_xray_findings_other",)},
        ),
        ("ECG", {"fields": ("ecg_findings", "ecg_findings_other",)},),
        ("ECHO", {"fields": ("echo_findings", "echo_findings_other",)},),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    filter_horizontal = ["chest_xray_findings", "ecg_findings", "echo_findings"]

    radio_fields = {
        "crf_status": admin.VERTICAL,
    }
