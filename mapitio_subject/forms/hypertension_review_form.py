from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import HypertensionReview


class HypertensionReviewFormValidator(FormValidator):
    pass


class HypertensionReviewForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = HypertensionReviewFormValidator

    class Meta:
        model = HypertensionReview
        fields = "__all__"
