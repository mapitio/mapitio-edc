from edc_consent.form_validators import SubjectConsentFormValidatorMixin
from edc_form_validators import FormValidator


class SubjectConsentFormValidator(SubjectConsentFormValidatorMixin, FormValidator):
    subject_screening_model = "mapitio_screening.subjectscreening"
