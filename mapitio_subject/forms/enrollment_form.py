from django import forms
from edc_form_validators import FormValidatorMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Enrollment


class EnrollmentFormValidator(FormValidator):
    pass


class EnrollmentForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = EnrollmentFormValidator

    class Meta:
        model = Enrollment
        fields = "__all__"
