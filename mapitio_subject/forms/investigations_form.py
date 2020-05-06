from django import forms
from edc_constants.constants import NORMAL, NOT_DONE, OTHER, YES
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Investigations


class InvestigationsFormValidator(FormValidator):
    def clean(self):

        for prefix in ["chest_xray", "ecg", "echo"]:

            self.applicable_if(
                YES,
                field=f"{prefix}_requested",
                field_applicable=f"{prefix}_findings_documented",
            )
            self.m2m_required_if(
                YES,
                field=f"{prefix}_findings_documented",
                m2m_field=f"{prefix}_findings",
            )
            self.m2m_single_selection_if(NOT_DONE, m2m_field=f"{prefix}_findings")
            self.m2m_single_selection_if(NORMAL, m2m_field=f"{prefix}_findings")
            self.m2m_other_specify(
                OTHER,
                m2m_field=f"{prefix}_findings",
                field_other=f"{prefix}_findings_other",
            )


class InvestigationsForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = InvestigationsFormValidator

    class Meta:
        model = Investigations
        fields = "__all__"
