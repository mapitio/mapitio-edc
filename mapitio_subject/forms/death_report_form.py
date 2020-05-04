from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import DEAD, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat
from mapitio_screening.models import SubjectScreening

from django.conf import settings
from ..models import DeathReport


class DeathReportFormValidator(FormValidator):
    def clean(self):
        enrollment = SubjectScreening.objects.get(
            subject_identifier=self.cleaned_data.get("subject_visit").subject_identifier
        )
        formatted_date = enrollment.clinic_registration_date.strftime(
            convert_php_dateformat(settings.SHORT_DATE_FORMAT)
        )

        if self.cleaned_data.get("death_date"):
            if (
                self.cleaned_data.get("death_date")
                <= enrollment.clinic_registration_date
            ):
                raise forms.ValidationError(
                    {
                        "death_date": (
                            f"Cannot be on or before the "
                            f"enrollment date ({formatted_date})."
                        )
                    }
                )
        self.required_if(YES, field="death_cause_known", field_required="death_cause")


class DeathReportForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = "__all__"
