from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Complications


class ComplicationsFormValidator(FormValidator):
    def clean(self):
        self.required_if(YES, field="stroke", field_required="stroke_dx_date"),
        self.required_if(
            YES, field="diabetic_foot", field_required="diabetic_foot_dx_date"
        ),
        self.required_if(
            YES, field="cardiomyopathy", field_required="cardiomyopathy_dx_date"
        ),
        self.required_if(
            YES,
            field="chronic_renal_failure",
            field_required="chronic_renal_failure_dx_date",
        ),
        self.required_if(
            YES,
            field="diabetic_retinopathy",
            field_required="diabetic_retinopathy_dx_date",
        ),
        self.required_if(
            YES,
            field="peripheral_vascular",
            field_required="peripheral_vascular_dx_date",
        ),
        self.required_if(
            YES,
            field="peripheral_neuropathy",
            field_required="peripheral_neuropathy_dx_date",
        ),
        self.required_if(
            YES, field="complications", field_required="complications_other"
        ),


class ComplicationsForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = ComplicationsFormValidator

    class Meta:
        model = Complications
        fields = "__all__"
