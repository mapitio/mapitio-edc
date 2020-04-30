from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import NcdFollowup


class NcdFollowupFormValidator(FormValidator):
    pass


class NcdFollowupForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NcdFollowupFormValidator

    class Meta:
        model = NcdFollowup
        fields = "__all__"
