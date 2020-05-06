from django.contrib import admin
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BiomedicalFollowupForm
from ..models import BiomedicalFollowup
from .fieldsets import (
    biomedical_fieldsets,
    biomedical_radio_fields,
)
from .modeladmin import CrfModelAdminMixin


@admin.register(BiomedicalFollowup, site=mapitio_subject_admin)
class BiomedicalFollowupAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin,
):
    additional_instructions = (
        "Complete for data recorded when patient last attended the clinic "
    )

    form = BiomedicalFollowupForm

    fieldsets = biomedical_fieldsets

    radio_fields = biomedical_radio_fields
