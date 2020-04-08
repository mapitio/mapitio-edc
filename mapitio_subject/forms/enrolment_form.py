from django import forms
from edc_form_validators import FormValidatorMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Enrolment


class EnrolmentFormValidator(FormValidator):
    pass


class EnrolmentForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = EnrolmentFormValidator

    class Meta:
        model = Enrolment
        fields = "__all__"
