from dateutil.relativedelta import relativedelta
from django import forms
from django.conf import settings
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_constants.constants import NEG, POS
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_utils import convert_php_dateformat
from mapitio_screening.models import SubjectScreening

from ..models import BiomedicalHistory


class BiomedicalFormValidator(FormValidator):
    def clean(self):

        for field_name in [
            "total_cholesterol",
            "ldl",
            "hdl",
            "triglycerides",
        ]:
            self.required_if_not_none(
                field=field_name,
                field_required=f"{field_name}_date",
                field_required_evaluate_as_int=True,
            )

        self.required_if_not_none(
            field="serum_urea",
            field_required="serum_urea_units",
            field_required_evaluate_as_int=True,
        )
        self.required_if_not_none(
            field="serum_urea",
            field_required="serum_urea_date",
            field_required_evaluate_as_int=True,
        )

        self.required_if_not_none(
            field="serum_creatinine",
            field_required="serum_creatinine_units",
            field_required_evaluate_as_int=True,
        )
        self.required_if_not_none(
            field="serum_creatinine",
            field_required="serum_creatinine_date",
            field_required_evaluate_as_int=True,
        )

        self.required_if_not_none(
            field="serum_uric_acid",
            field_required="serum_uric_acid_units",
            field_required_evaluate_as_int=True,
        )
        self.required_if_not_none(
            field="serum_creatinine",
            field_required="serum_uric_acid_date",
            field_required_evaluate_as_int=True,
        )

        for field_name in [
            "ast",
            "alt",
            "alp",
            "amylase",
            "ggt",
        ]:
            self.required_if_not_none(
                field=field_name,
                field_required=f"{field_name}_date",
                field_required_evaluate_as_int=True,
            )

        self.required_if_not_none(
            field="albumin",
            field_required="albumin_units",
            field_required_evaluate_as_int=True,
        )
        self.required_if_not_none(
            field="albumin",
            field_required="albumin_date",
            field_required_evaluate_as_int=True,
        )

        self.required_if_not_none(
            field="cd4", field_required="cd4_date", field_required_evaluate_as_int=True
        )
        self.required_if_not_none(
            field="vl", field_required="vl_date", field_required_evaluate_as_int=True
        )

        for field_name in [
            "hbsag",
            "hcv",
        ]:
            self.required_if(
                POS, NEG, field=field_name, field_required=f"{field_name}_date",
            )


class BiomedicalHistoryFormValidator(BiomedicalFormValidator):
    def clean(self):
        super().clean()
        enrollment = SubjectScreening.objects.get(
            subject_identifier=self.cleaned_data.get("subject_visit").subject_identifier
        )
        formatted_date = enrollment.clinic_registration_date.strftime(
            convert_php_dateformat(settings.SHORT_DATE_FORMAT)
        )

        for fld in BiomedicalHistory._meta.get_fields():
            if fld.name.endswith("_date"):
                if self.cleaned_data.get(fld.name):
                    if self.cleaned_data.get(
                        fld.name
                    ) > enrollment.clinic_registration_date + relativedelta(months=6):
                        raise forms.ValidationError(
                            {
                                fld.name: (
                                    f"Cannot be more than 6 months after the "
                                    f"enrollment date ({formatted_date})."
                                )
                            }
                        )


class BiomedicalHistoryForm(CrfModelFormMixin, ActionItemFormMixin, forms.ModelForm):
    form_validator_cls = BiomedicalHistoryFormValidator

    class Meta:
        model = BiomedicalHistory
        fields = "__all__"
