from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import mapitio_subject_admin
from ..forms import EnrolmentForm
from ..models import Enrolment


@admin.register(Enrolment, site=mapitio_subject_admin)
class EnrolmentAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):
    form = EnrolmentForm

    fieldsets = (
        (
            "Enrolment",
            {
                "fields": (
                    "report_datetime",
                    "first_name",
                    "last_name",
                    "initials",
                    "dob",
                    "is_dob_estimated",
                    "gender",
                    "identity",
                    "identity_type",
                    "confirm_identity",
                    "clinic_registration_datetime",
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
