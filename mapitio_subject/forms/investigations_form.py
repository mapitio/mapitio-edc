from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import NOT_DONE, OTHER
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator

from ..models import Investigations


class InvestigationsFormValidator(FormValidator):
    def clean(self):
        self.m2m_single_selection_if(NOT_DONE, m2m_field="chest_xray_findings")
        self.m2m_other_specify(
            OTHER,
            m2m_field="chest_xray_findings",
            field_other="chest_xray_findings_other",
        )

        self.m2m_single_selection_if(NOT_DONE, m2m_field="ecg_findings")
        self.m2m_other_specify(
            OTHER, m2m_field="ecg_findings", field_other="ecg_findings_other",
        )

        self.m2m_single_selection_if(NOT_DONE, m2m_field="echo_findings")
        self.m2m_other_specify(
            OTHER, m2m_field="echo_findings", field_other="echo_findings_other",
        )


class InvestigationsForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = InvestigationsFormValidator

    class Meta:
        model = Investigations
        fields = "__all__"
