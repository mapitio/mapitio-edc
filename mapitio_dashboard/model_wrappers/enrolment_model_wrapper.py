from edc_consent import ConsentModelWrapperMixin
from edc_model_wrapper import ModelWrapper
from edc_subject_model_wrappers import SubjectConsentModelWrapper as BaseModelWrapper


class EnrolmentConsentModelWrapper(BaseModelWrapper):
    @property
    def querystring(self):
        return (
            f"cancel=mapitio_dashboard:enrolment_listboard_url,"
            f"enrolment_identifier&{super().querystring}"
        )


class EnrolmentModelWrapper(ConsentModelWrapperMixin, ModelWrapper):

    consent_model_wrapper_cls = EnrolmentConsentModelWrapper
    model = "mapitio_subject.enrolment"
    next_url_attrs = ["enrolment_identifier"]
    next_url_name = "enrolment_listboard_url"
    querystring_attrs = ["gender"]

    @property
    def human_enrolment_identifier(self):
        human = None
        if self.enrolment_identifier:
            human = f"{self.enrolment_identifier[0:4]}-{self.enrolment_identifier[4:]}"
        return human or self.enrolment_identifier

    @property
    def human_identity(self):
        human = None
        if self.identity:
            human = f"{self.identity[0:4]}-{self.identity[4:]}"
        return human or self.identity
