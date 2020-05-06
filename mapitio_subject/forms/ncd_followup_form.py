from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from ..models import NcdFollowup
from .ncd_history_form import NcdFormValidator


class NcdFollowupFormValidator(NcdFormValidator):
    history = False


class NcdFollowupForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NcdFollowupFormValidator

    class Meta:
        model = NcdFollowup
        fields = "__all__"
