from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import BiomedicalFollowupForm
from ..models import BiomedicalFollowup
from .modeladmin import CrfModelAdminMixin


@admin.register(BiomedicalFollowup, site=mapitio_subject_admin)
class BiomedicalFollowupAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):
    form = BiomedicalFollowupForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime", "drawn_date")}),
        (
            "Lipid Profile",
            {"fields": ("total_cholesterol", "ldl", "hdl", "triglycerides")},
        ),
        (
            "Renal Profile",
            {
                "fields": (
                    "serum_urea",
                    "serum_urea_units",
                    "serum_creatinine",
                    "serum_creatinine_units",
                    "serum_uric_acid",
                    "serum_uric_acid_units",
                    "egfr",
                ),
            },
        ),
        (
            "Liver Profile",
            {
                "fields": (
                    "ast",
                    "alt",
                    "alp",
                    "amylase",
                    "ggt",
                    "albumin",
                    "albumin_units",
                )
            },
        ),
        ("HIV", {"fields": ("cd4", "cd4_date", "vl", "vl_date",),},),
        ("Other Infectious Diseases", {"fields": ("hbsag", "hcv",),},),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "serum_urea_units": admin.VERTICAL,
        "serum_creatinine_units": admin.VERTICAL,
        "serum_uric_acid_units": admin.VERTICAL,
        "albumin_units": admin.VERTICAL,
        "hbsag": admin.VERTICAL,
        "hcv": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
