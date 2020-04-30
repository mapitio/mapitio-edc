from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Indicators


class IndicatorsFormValidator(FormValidator):
    def clean(self):

        self.required_if_not_none(
            field="sys_blood_pressure", field_required="dia_blood_pressure"
        )
        self.required_if_not_none(field="glucose", field_required="glucose_units")
        self.required_if_not_none(field="glucose", field_required="glucose_fasting")


class IndicatorsForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = IndicatorsFormValidator

    class Meta:
        model = Indicators
        fields = "__all__"
