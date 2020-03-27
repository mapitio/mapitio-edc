from edc_consent.constants import HOSPITAL_NUMBER, CLINIC_NUMBER
from edc_constants.constants import MOBILE_NUMBER, OTHER

IDENTITY_TYPE = (
    ("country_id", "Country ID number"),
    ("drivers", "Driver's license"),
    ("passport", "Passport"),
    (CLINIC_NUMBER, "Clinic number"),
    (HOSPITAL_NUMBER, "Hospital number"),
    (MOBILE_NUMBER, "Mobile number"),
    (OTHER, "Other"),
)
