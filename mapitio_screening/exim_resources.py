from edc_crf import NonCrfModelResource
from .models import SubjectScreening


class SubjectScreeningResource(NonCrfModelResource):
    class Meta(NonCrfModelResource.Meta):
        model = SubjectScreening
        exclude = (
            "hospital_identifier",
            "confirm_hospital_identifier",
            "ctc_identifier",
            "confirm_ctc_identifier",
            "hostname_modified",
            "device_created",
            "device_modified",
            "site",
            "subject_identifier_as_pk",
            "subject_identifier_aka",
            "slug",
            "first_name",
            "last_name",
            "guardian_name",
            "file_number",
            "eligible",
            "consent_ability",
            "unsuitable_for_study",
            "reasons_unsuitable",
            "unsuitable_agreed",
            "reasons_ineligible",
            "screening_consent",
            "selection_method",
            "clinic_type",
        )
