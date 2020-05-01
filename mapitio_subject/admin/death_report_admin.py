from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import DeathReportForm
from ..models import DeathReport
from .modeladmin import CrfModelAdminMixin


@admin.register(DeathReport, site=mapitio_subject_admin)
class DeathReportAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = DeathReportForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Details",
            {"fields": ("death_date", "death_date_estimated", "death_cause"),},
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "death_date_estimated": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
