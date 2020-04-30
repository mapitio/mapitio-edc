from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import OTHER
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat
from mapitio_screening.models import SubjectScreening

from django.conf import settings
from ..models import HivHistory


class HivHistoryFormValidator(FormValidator):
    def clean(self):
        if self.cleaned_data.get("hiv_pos_date"):
            enrollment = SubjectScreening.objects.get(
                subject_identifier=self.cleaned_data.get(
                    "subject_visit"
                ).subject_identifier
            )
            if (
                self.cleaned_data.get("hiv_pos_date")
                > enrollment.clinic_registration_date
            ):
                formatted_date = enrollment.clinic_registration_date.strftime(
                    convert_php_dateformat(settings.SHORT_DATE_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        "hiv_pos_date": (
                            f"Cannot be after clinic enrollment date. "
                            f"({formatted_date})"
                        )
                    }
                )
            if self.cleaned_data.get("hiv_pos_date") > self.cleaned_data.get(
                "arv_initiation_date"
            ):
                formatted_date = self.cleaned_data.get("hiv_pos_date").strftime(
                    convert_php_dateformat(settings.SHORT_DATE_FORMAT)
                )
                raise forms.ValidationError(
                    {
                        "arv_initiation_date": (
                            f"Cannot be before HIV diagnosis date. "
                            f"({formatted_date})"
                        )
                    }
                )

        self.validate_other_specify(field="arv_regimen")


class HivHistoryForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = HivHistoryFormValidator

    class Meta:
        model = HivHistory
        fields = "__all__"
