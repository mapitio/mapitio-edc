from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import BiomedicalHistory


class BiomedicalFormValidator(FormValidator):
    def clean(self):
        self.required_if_not_none(field="serum_urea", field_required="serum_urea_units")
        self.required_if_not_none(
            field="serum_creatinine", field_required="serum_creatinine_units"
        )
        self.required_if_not_none(
            field="serum_uric_acid", field_required="serum_uric_acid_units"
        )
        self.required_if_not_none(field="albumin", field_required="albumin_units")
        self.required_if_not_none(field="cd4", field_required="cd4_date")
        self.required_if_not_none(field="vl", field_required="vl_date")


class BiomedicalHistoryForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = BiomedicalFormValidator

    class Meta:
        model = BiomedicalHistory
        fields = "__all__"
