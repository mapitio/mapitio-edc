from django_audit_fields import audit_fieldset_tuple
from django.contrib import admin

comment_fieldset_tuple = ("Comments", {"fields": ("crf_status", "comments")})

biomedical_fieldsets = (
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

biomedical_radio_fields = {
    "serum_urea_units": admin.VERTICAL,
    "serum_creatinine_units": admin.VERTICAL,
    "serum_uric_acid_units": admin.VERTICAL,
    "albumin_units": admin.VERTICAL,
    "hbsag": admin.VERTICAL,
    "vl_detectable": admin.VERTICAL,
    "hcv": admin.VERTICAL,
    "crf_status": admin.VERTICAL,
}
