from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from django.utils.safestring import mark_safe

from ..admin_site import mapitio_subject_admin
from ..exim_resources import FollowupResource
from ..forms import FollowupForm
from ..models import Followup
from .modeladmin import CrfModelAdminMixin


@admin.register(Followup, site=mapitio_subject_admin)
class FollowupAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = FollowupForm

    resource_class = FollowupResource

    additional_instructions = mark_safe(
        "<span style='color:#ff8000'>Complete for data as of the patient's last attended clinic visit</span>"
    )

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Follow Up (as of the last clinic visit)",
            {
                "fields": (
                    "alive",
                    "in_care",
                    "reason_not_in_care",
                    "reason_not_in_care_other",
                ),
            },
        ),
        (
            "Next appointment",
            {"fields": ("has_next_appointment", "next_appointment_date",)},
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "alive": admin.VERTICAL,
        "in_care": admin.VERTICAL,
        "reason_not_in_care": admin.VERTICAL,
        "has_next_appointment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
