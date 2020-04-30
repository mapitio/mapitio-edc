from django import forms
from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class SubjectScreeningFormValidator(FormValidator):
    def clean(self):
        if (
            self.cleaned_data.get("age_in_years")
            and self.cleaned_data.get("age_in_years") < 18
        ):
            raise forms.ValidationError(
                {"age_in_years": "Participant must be at least 18 years old."}
            )

        if self.cleaned_data.get("hospital_identifier") and self.cleaned_data.get(
            "confirm_hospital_identifier"
        ):
            if self.cleaned_data.get("hospital_identifier") != self.cleaned_data.get(
                "confirm_hospital_identifier"
            ):
                raise forms.ValidationError({"confirm_hospital_identifier": "Mismatch"})

        if self.cleaned_data.get("hospital_identifier") == self.cleaned_data.get(
            "ctc_identifier"
        ):
            raise forms.ValidationError(
                {"ctc_identifier": "Cannot be the same as the hospital identifier"}
            )

        self.required_if_true(
            self.cleaned_data.get("ctc_identifier"),
            field_required="confirm_ctc_identifier",
        )

        if self.cleaned_data.get("ctc_identifier") and self.cleaned_data.get(
            "confirm_ctc_identifier"
        ):
            if self.cleaned_data.get("ctc_identifier") != self.cleaned_data.get(
                "confirm_ctc_identifier"
            ):
                raise forms.ValidationError({"confirm_ctc_identifier": "Mismatch"})

        if self.cleaned_data.get("clinic_registration_date"):
            if self.cleaned_data.get("clinic_registration_date").year < 2010:
                raise forms.ValidationError(
                    {"clinic_registration_date": "Cannot be before 2010"}
                )
            if self.cleaned_data.get("clinic_registration_date").year > 2014:
                raise forms.ValidationError(
                    {"clinic_registration_date": "Cannot be after 2014"}
                )

        if self.cleaned_data.get("clinic_registration_date") and self.cleaned_data.get(
            "last_clinic_date"
        ):
            if self.cleaned_data.get("last_clinic_date") < self.cleaned_data.get(
                "clinic_registration_date"
            ):

                raise forms.ValidationError(
                    {"last_clinic_date": "Cannot be before enrollment date"}
                )
