from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import mapitio_subject_admin
from ..forms import EnrollmentForm
from ..models import Enrollment


@admin.register(Enrollment, site=mapitio_subject_admin)
class EnrollmentAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    form = EnrollmentForm

    fieldsets = (
        (
            "Enrollment",
            {
                "fields": (
                    "report_datetime",
                    "first_name",
                    "last_name",
                    "initials",
                    "age_in_years",
                    "dob",
                    "is_dob_estimated",
                    "gender",
                    "identity",
                    "confirm_identity",
                    "clinic_registration_date",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "identity_type": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
