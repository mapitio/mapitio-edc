from django import forms
from django.conf import settings
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_utils import convert_php_dateformat
from mapitio_screening.models import SubjectScreening

from ..models import BiomedicalFollowup
from .biomedical_history_form import BiomedicalFormValidator


class BiomedicalFollowupFormValidator(BiomedicalFormValidator):
    def clean(self):
        super().clean()
        enrollment = SubjectScreening.objects.get(
            subject_identifier=self.cleaned_data.get("subject_visit").subject_identifier
        )
        formatted_date = enrollment.clinic_registration_date.strftime(
            convert_php_dateformat(settings.SHORT_DATE_FORMAT)
        )
        for fld in BiomedicalFollowup._meta.get_fields():
            if fld.name.endswith("_date"):
                if self.cleaned_data.get(fld.name):
                    if (
                        self.cleaned_data.get(fld.name)
                        <= enrollment.clinic_registration_date
                    ):
                        raise forms.ValidationError(
                            {
                                fld.name: (
                                    f"Cannot be before the "
                                    f"enrollment date ({formatted_date})."
                                )
                            }
                        )


class BiomedicalFollowupForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = BiomedicalFollowupFormValidator

    class Meta:
        model = BiomedicalFollowup
        fields = "__all__"
