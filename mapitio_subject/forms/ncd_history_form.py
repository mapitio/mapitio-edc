from django import forms
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat

from django.conf import settings
from mapitio_screening.models import SubjectScreening

from ..models import NcdHistory


class NcdHistoryFormValidator(FormValidator):
    def clean(self):
        enrollment = SubjectScreening.objects.get(
            subject_identifier=self.cleaned_data.get("subject_visit").subject_identifier
        )

        # diabetes
        self.applicable_if(
            YES, field="diabetic", field_applicable="diabetes_dx_date_known"
        )
        self.required_if(YES, field="diabetic", field_required="diabetes_dx_date")

        if self.cleaned_data.get("diabetes_dx_date"):
            if (
                self.cleaned_data.get("diabetes_dx_date")
                > enrollment.clinic_registration_date
            ):
                formatted_date = enrollment.clinic_registration_date.strftime(
                    convert_php_dateformat(settings.SHORT_DATE_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        "diabetes_dx_date": (
                            f"Cannot be after clinic enrollment date. "
                            f"({formatted_date})"
                        )
                    }
                )
        self.applicable_if(
            YES, field="diabetic", field_applicable="diabetes_dx_date_estimated"
        )
        self.m2m_applicable_if(YES, field="diabetic", m2m_field="diabetes_rx")
        self.m2m_other_specify(
            OTHER, m2m_field="diabetes_rx", field_other="other_diabetes_rx"
        )

        # hypertension
        self.applicable_if(
            YES, field="hypertensive", field_applicable="hypertension_dx_date_known"
        )
        self.required_if(
            YES, field="hypertensive", field_required="hypertension_dx_date"
        )
        if self.cleaned_data.get("hypertension_dx_date"):
            if (
                self.cleaned_data.get("hypertension_dx_date")
                > enrollment.clinic_registration_date
            ):
                formatted_date = enrollment.clinic_registration_date.strftime(
                    convert_php_dateformat(settings.SHORT_DATE_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        "hypertension_dx_date": (
                            f"Cannot be after clinic enrollment date. "
                            f"({formatted_date})"
                        )
                    }
                )
        self.applicable_if(
            YES, field="hypertensive", field_applicable="hypertension_dx_date_estimated"
        )
        self.m2m_applicable_if(YES, field="hypertensive", m2m_field="hypertension_rx")
        self.m2m_other_specify(
            OTHER, m2m_field="hypertension_rx", field_other="other_hypertension_rx"
        )

        # cholesterol
        self.m2m_applicable_if(
            YES, field="takes_cholesterol_rx", m2m_field="cholesterol_rx"
        )
        self.m2m_other_specify(
            OTHER, m2m_field="cholesterol_rx", field_other="other_cholesterol_rx"
        )


class NcdHistoryForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NcdHistoryFormValidator

    class Meta:
        model = NcdHistory
        fields = "__all__"
