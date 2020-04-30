from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import IndicatorsForm
from ..models import Indicators
from .modeladmin import CrfModelAdminMixin


@admin.register(Indicators, site=mapitio_subject_admin)
class IndicatorsAdmin(CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin):

    additional_instructions = (
        "Complete for data recorded when patient first attended the clinic "
    )

    form = IndicatorsForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Indicators",
            {
                "fields": (
                    "height",
                    "weight",
                    "waist_circumference",
                    "sys_blood_pressure",
                    "dia_blood_pressure",
                    "glucose",
                    "glucose_units",
                    "glucose_fasting",
                ),
            },
        ),
        comment_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "glucose_units": admin.VERTICAL,
        "glucose_fasting": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
