from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Investigations


class InvestigationsFormValidator(FormValidator):
    pass


class InvestigationsForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = InvestigationsFormValidator

    class Meta:
        model = Investigations
        fields = "__all__"
