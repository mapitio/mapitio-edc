from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from mapitio_screening.models import SubjectScreening

from ..models import NcdFollowup
from .ncd_history_form import NcdFormValidator


class NcdFollowupFormValidator(FormValidator):
    def clean(self):
        enrollment = SubjectScreening.objects.get(
            subject_identifier=self.cleaned_data.get("subject_visit").subject_identifier
        )


class NcdFollowupFormValidator(NcdFormValidator):
    history = False


class NcdFollowupForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = NcdFollowupFormValidator

    class Meta:
        model = NcdFollowup
        fields = "__all__"
