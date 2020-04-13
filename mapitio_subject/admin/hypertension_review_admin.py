from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import HypertensionReviewForm
from ..models import HypertensionReview
from .fieldsets import comment_fieldset_tuple
from .modeladmin import CrfModelAdminMixin


@admin.register(HypertensionReview, site=mapitio_subject_admin)
class HypertensionReviewAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = HypertensionReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Hypertension Review",
            {"fields": ("dx_at_registration", "dx_date", "dx_date_estimated",),},
        ),
        ("Treatment", {"fields": ("rx_start_date", "rx_initial", "rx_current")}),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "dx_at_registration": admin.VERTICAL,
        "dx_date_estimated": admin.VERTICAL,
        "rx_start_date_estimated": admin.VERTICAL,
        "rx_initial": admin.VERTICAL,
        "rx_current": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
