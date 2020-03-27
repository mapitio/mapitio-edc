from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import BaselineData


class BaselineDataFormValidator(FormValidator):
    pass


class BaselineDataForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = BaselineDataFormValidator

    class Meta:
        model = BaselineData
        fields = "__all__"
