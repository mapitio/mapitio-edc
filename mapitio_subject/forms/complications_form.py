from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Complications


class ComplicationsFormValidator(FormValidator):
    pass


class ComplicationsForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = ComplicationsFormValidator

    class Meta:
        model = Complications
        fields = "__all__"
