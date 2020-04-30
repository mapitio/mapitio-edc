from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..models import BiomedicalFollowup
from .biomedical_history_form import BiomedicalFormValidator


class BiomedicalFollowupForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = BiomedicalFormValidator

    class Meta:
        model = BiomedicalFollowup
        fields = "__all__"
