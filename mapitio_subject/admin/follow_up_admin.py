from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin import CrfModelAdminMixin


@admin.register(FollowUp, site=mapitio_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = FollowUpForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Details",
            {
                "fields": (
                    "last_seen_date",
                    "in_care",
                    "reason_not_in_care",
                    "reason_not_in_care_other",
                ),
            },
        ),
        (
            "Survival Status",
            {"fields": ("death_date", "death_date_estimated", "death_cause"),},
        ),
        (
            "Next appointment",
            {"fields": ("has_next_appointment", "next_appointment_date",),},
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "in_care": admin.VERTICAL,
        "reason_not_in_care": admin.VERTICAL,
        "death_date_estimated": admin.VERTICAL,
        "has_next_appointment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
