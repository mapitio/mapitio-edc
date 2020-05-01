from django import forms
from django.core.exceptions import ImproperlyConfigured
from edc_constants.constants import OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat

from django.conf import settings
from mapitio_screening.models import SubjectScreening

from ..models import NcdHistory


class NcdFormValidator(FormValidator):
    history = None

    def raise_on_invalid_dx_date(self, dx_date_fld, registration_date):
        formatted_date = registration_date.strftime(
            convert_php_dateformat(settings.SHORT_DATE_FORMAT)
        )
        if self.history is True:
            if self.cleaned_data.get(dx_date_fld) > registration_date:
                raise forms.ValidationError(
                    {
                        dx_date_fld: (
                            f"Cannot be after clinic enrollment date. "
                            f"({formatted_date})"
                        )
                    }
                )
        elif self.history is False:
            if self.cleaned_data.get(dx_date_fld) < registration_date:
                raise forms.ValidationError(
                    {
                        dx_date_fld: (
                            f"Cannot be before clinic enrollment date. "
                            f"({formatted_date})"
                        )
                    }
                )
        else:
            raise ImproperlyConfigured(
                f"Expected `history` attribute to be True or False. See `{self.__class__.__name__}`"
            )
        return None

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
            self.raise_on_invalid_dx_date(
                "diabetes_dx_date", enrollment.clinic_registration_date
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
            self.raise_on_invalid_dx_date(
                "hypertension_dx_date", enrollment.clinic_registration_date
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


class NcdHistoryFormValidator(NcdFormValidator):
    history = True


class NcdHistoryForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NcdHistoryFormValidator

    class Meta:
        model = NcdHistory
        fields = "__all__"
