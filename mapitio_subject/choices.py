from edc_consent.constants import HOSPITAL_NUMBER, NATIONAL_IDENTIFIER
from edc_constants.constants import (
    FASTING,
    NON_FASTING,
    NORMAL,
    OTHER,
    HOSPITAL_NOTES,
    NOT_APPLICABLE,
)
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT

CRF_STATUS = (
    ("incomplete", "Incomplete (some data pending)"),
    ("complete", "Complete"),
)
FASTING_CHOICES = ((FASTING, "Fasting"), (NON_FASTING, "Non-fasting"))

CHEST_XRAY_CHOICES = (
    (NORMAL, "Normal"),
    ("pneumonia", "Pneumonia"),
    ("pcp", "PCP"),
    ("cardiomegaly", "Cardiomegaly"),
    ("pleural_effusion", "Pleural effusion"),
)

ECG = (
    (NORMAL, "Normal"),
    ("left_ventricular_hypertrophy", "Left ventricular hypertrophy"),
    ("ischaemic_heart_disease", "Ischaemic heart disease"),
    ("heart_arrhythmias", "Heart arrhythmias"),
    (OTHER, "Other"),
)

ECHO = (
    (NORMAL, "Normal"),
    ("left_ventricular_hypertrophy", "Left ventricular hypertrophy"),
    ("dystolic_dysfunction", "Dystolic dysfunction"),
    ("cardiomyopathy ", "Cardiomyopathy "),
    (OTHER, "Other"),
)


IDENTITY_TYPE = (
    (HOSPITAL_NUMBER, "Hospital Identifier"),
    (NATIONAL_IDENTIFIER, "National Identifier"),
    ("DRIVERS", "Driver's License"),
    ("PASSPORT", "Passport"),
    (OTHER, "Other"),
)

INFO_SOURCE = (
    (HOSPITAL_NOTES, "Hospital notes"),
    ("outpatient_cards", "Outpatient cards"),
    ("patient", "Patient"),
    ("collateral_history", "Collateral History from relative/guardian"),
    (OTHER, "Other"),
)

VISIT_UNSCHEDULED_REASON = (
    ("patient_unwell_outpatient", "Patient unwell (outpatient)"),
    ("patient_hospitalised", "Patient hospitalised"),
    ("routine_non_study", "Routine appointment (non-study)"),
    ("recurrence_symptoms", "Recurrence of symptoms"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

VISIT_REASON = (
    (SCHEDULED, "Scheduled visit"),
    (UNSCHEDULED, "Unscheduled visit"),
    (MISSED_VISIT, "Missed visit"),
)
