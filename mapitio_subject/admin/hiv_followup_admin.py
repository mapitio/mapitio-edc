from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import HivFollowupForm
from ..models import HivFollowup
from .modeladmin import CrfModelAdminMixin


@admin.register(HivFollowup, site=mapitio_subject_admin)
class HivFollowupAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    additional_instructions = mark_safe(
        "<span style='color:#ff8000'>Complete for data as of the patient's last attended clinic visit</span>"
    )

    form = HivFollowupForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Last Recorded ARV Regimen",
            {
                "fields": (
                    "arv_modification",
                    "arv_modification_date",
                    "arv_regimen",
                    "arv_regimen_other",
                ),
            },
        ),
        ("DTG-Based Regimen", {"fields": ("dtg_switched", "dtg_switched_date",),},),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "arv_modification": admin.VERTICAL,
        "arv_regimen": admin.VERTICAL,
        "dtg_switched": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
