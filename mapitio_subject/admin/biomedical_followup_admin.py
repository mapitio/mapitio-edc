from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from mapitio_subject.admin.fieldsets import comment_fieldset_tuple

from ..admin_site import mapitio_subject_admin
from ..forms import BiomedicalFollowupForm
from ..models import BiomedicalFollowup
from .modeladmin import BiomedicalModelAdminMixin, CrfModelAdminMixin


@admin.register(BiomedicalFollowup, site=mapitio_subject_admin)
class BiomedicalFollowupAdmin(
    BiomedicalModelAdminMixin,
    CrfModelAdminMixin,
    FormLabelModelAdminMixin,
    SimpleHistoryAdmin,
):
    additional_instructions = (
        "Complete for data recorded when patient last attended the clinic "
    )

    form = BiomedicalFollowupForm
