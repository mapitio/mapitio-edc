from django.contrib import admin
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin

from ..admin_site import mapitio_subject_admin
from ..forms import BiomedicalHistoryForm
from ..models import BiomedicalHistory
from .modeladmin import BiomedicalModelAdminMixin, CrfModelAdminMixin


@admin.register(BiomedicalHistory, site=mapitio_subject_admin)
class BiomedicalHistoryAdmin(
    BiomedicalModelAdminMixin,
    CrfModelAdminMixin,
    FormLabelModelAdminMixin,
    SimpleHistoryAdmin,
):
    additional_instructions = (
        "Complete for data recorded when patient first attended the clinic "
    )

    form = BiomedicalHistoryForm
