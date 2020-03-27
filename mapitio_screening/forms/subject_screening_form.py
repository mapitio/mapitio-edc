from django import forms
from edc_form_validators import FormValidatorMixin
from edc_screening.modelform_mixins import AlreadyConsentedFormMixin

from ..form_validators import SubjectScreeningFormValidator
from ..models import SubjectScreening


class SubjectScreeningForm(
    AlreadyConsentedFormMixin, FormValidatorMixin, forms.ModelForm
):
    form_validator_cls = SubjectScreeningFormValidator

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = SubjectScreening
        fields = [
            "screening_consent",
            "selection_method",
            "clinic_type",
            "report_datetime",
            "initials",
            "gender",
            "age_in_years",
            "qualifying_condition",
            "lives_nearby",
            "requires_acute_care",
            "unsuitable_for_study",
            "reasons_unsuitable",
            "unsuitable_agreed",
        ]
