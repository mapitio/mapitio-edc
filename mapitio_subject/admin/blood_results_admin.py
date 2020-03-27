from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BloodResultsForm
from ..models import BloodResults
from .modeladmin import CrfModelAdminMixin


@admin.register(BloodResults, site=mapitio_subject_admin)
class BloodResultsAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BloodResultsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        ("Blood Results", {"fields": ("crf_status", "comment",),},),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
    }
