from django import forms
from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class SubjectScreeningFormValidator(FormValidator):
    def clean(self):
        if (
            not self.cleaned_data.get("screening_consent")
            or self.cleaned_data.get("screening_consent") != YES
        ):
            raise forms.ValidationError(
                {
                    "screening_consent": (
                        "You may NOT screen this subject without their verbal consent."
                    )
                }
            )
        if (
            self.cleaned_data.get("age_in_years")
            and self.cleaned_data.get("age_in_years") < 18
        ):
            raise forms.ValidationError(
                {"age_in_years": "Participant must be at least 18 years old."}
            )
        self.required_if(
            YES, field="unsuitable_for_study", field_required="reasons_unsuitable"
        )

        self.applicable_if(
            YES, field="unsuitable_for_study", field_applicable="unsuitable_agreed"
        )

        if self.cleaned_data.get("unsuitable_agreed") == NO:
            raise forms.ValidationError(
                {
                    "unsuitable_agreed": (
                        "The study coordinator MUST agree with your assessment. "
                        "Please discuss before continuing."
                    )
                }
            )
