from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import (
    ModelAdminSubjectDashboardMixin,
    ModelAdminCrfDashboardMixin,
)
from .fieldsets import comment_fieldset_tuple


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(ModelAdminCrfDashboardMixin):
    def get_list_display(self, request):
        super().get_list_display(request)
        if "crf_status" not in self.list_display:
            self.list_display = list(self.list_display)
            self.list_display.append("crf_status")
        return self.list_display

    def get_list_filter(self, request):
        super().get_list_filter(request)
        if "crf_status" not in self.list_filter:
            self.list_filter = list(self.list_filter)
            self.list_filter.insert(0, "crf_status")
        return self.list_filter


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):

    pass


class BiomedicalModelAdminMixin:
    additional_instructions = (
        "Complete for data recorded when patient first attended the clinic "
    )

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Lipid Profile",
            {
                "fields": (
                    "total_cholesterol",
                    "total_cholesterol_date",
                    "ldl",
                    "ldl_date",
                    "hdl",
                    "hdl_date",
                    "triglycerides",
                    "triglycerides_date",
                )
            },
        ),
        (
            "Renal Profile",
            {
                "fields": (
                    "serum_urea",
                    "serum_urea_units",
                    "serum_urea_date",
                    "serum_creatinine",
                    "serum_creatinine_units",
                    "serum_creatinine_date",
                    "serum_uric_acid",
                    "serum_uric_acid_units",
                    "serum_uric_acid_date",
                    "egfr",
                ),
            },
        ),
        (
            "Liver Profile",
            {
                "fields": (
                    "ast",
                    "ast_date",
                    "alt",
                    "alt_date",
                    "alp",
                    "alp_date",
                    "amylase",
                    "amylase_date",
                    "ggt",
                    "ggt_date",
                    "albumin",
                    "albumin_units",
                    "albumin_date",
                )
            },
        ),
        ("HIV", {"fields": ("cd4", "cd4_date", "vl_detectable", "vl", "vl_date",)},),
        (
            "Other Infectious Diseases",
            {"fields": ("hbsag", "hbsag_date", "hcv", "hcv_date")},
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "serum_urea_units": admin.VERTICAL,
        "serum_creatinine_units": admin.VERTICAL,
        "serum_uric_acid_units": admin.VERTICAL,
        "albumin_units": admin.VERTICAL,
        "hbsag": admin.VERTICAL,
        "vl_detectable": admin.VERTICAL,
        "hcv": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
