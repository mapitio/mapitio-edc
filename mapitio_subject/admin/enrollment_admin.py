from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import EnrollmentForm
from ..models import Enrollment
from .modeladmin import CrfModelAdminMixin


@admin.register(Enrollment, site=mapitio_subject_admin)
class EnrollmentAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):
    form = EnrollmentForm

    fieldsets = (
        (
            "Enrollment",
            {
                "fields": (
                    "report_datetime",
                    "initials",
                    "dob",
                    "is_dob_estimated",
                    "gender",
                    "identity",
                    "identity_type",
                    "confirm_identity",
                    "clinic_registration_datetime",
                    "crf_status",
                    "comments",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "identity_type": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "gender": admin.VERTICAL,
    }
