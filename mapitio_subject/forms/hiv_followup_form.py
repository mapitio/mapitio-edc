from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HivFollowup


class HivFollowupFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            YES, field="arv_modification", field_required="arv_modification_date"
        )

        self.applicable_if(
            YES, field="arv_modification", field_applicable="arv_regimen"
        )

        self.validate_other_specify(
            field="arv_regimen", other_specify_field="arv_regimen_other"
        )

        self.required_if(YES, field="dtg_switched", field_required="dtg_switched_date")


class HivFollowupForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = HivFollowupFormValidator

    class Meta:
        model = HivFollowup
        fields = "__all__"
