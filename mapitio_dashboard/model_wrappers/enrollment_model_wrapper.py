from edc_consent import ConsentModelWrapperMixin
from edc_model_wrapper import ModelWrapper
from edc_subject_model_wrappers import SubjectConsentModelWrapper as BaseModelWrapper


class EnrollmentConsentModelWrapper(BaseModelWrapper):
    @property
    def querystring(self):
        return (
            f"cancel=mapitio_dashboard:enrollment_listboard_url,"
            f"enrollment_identifier&{super().querystring}"
        )


class EnrollmentModelWrapper(ConsentModelWrapperMixin, ModelWrapper):

    consent_model_wrapper_cls = EnrollmentConsentModelWrapper
    model = "mapitio_subject.enrollment"
    next_url_attrs = ["enrollment_identifier"]
    next_url_name = "enrollment_listboard_url"
    querystring_attrs = ["gender"]

    @property
    def human_enrollment_identifier(self):
        human = None
        if self.enrollment_identifier:
            human = (
                f"{self.enrollment_identifier[0:4]}-{self.enrollment_identifier[4:]}"
            )
        return human or self.enrollment_identifier

    @property
    def human_identity(self):
        human = None
        if self.identity:
            human = f"{self.identity[0:4]}-{self.identity[4:]}"
        return human or self.identity
