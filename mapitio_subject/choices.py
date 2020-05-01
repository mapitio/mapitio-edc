from edc_consent.constants import HOSPITAL_NUMBER, NATIONAL_IDENTIFIER
from edc_constants.constants import (
    COMPLETE,
    DEAD,
    FASTING,
    HELD,
    INCOMPLETE,
    INITIAL,
    LOST_TO_FOLLOWUP,
    MODIFIED,
    NON_FASTING,
    NONE,
    NORMAL,
    OTHER,
    HOSPITAL_NOTES,
    NOT_APPLICABLE,
    STOPPED,
)
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT

from .constants import DIABETES, HYPERTENSION

CRF_STATUS = (
    (INCOMPLETE, "Incomplete (some data pending)"),
    (COMPLETE, "Complete"),
)
FASTING_CHOICES = (
    (FASTING, "Fasting"),
    (NON_FASTING, "Non-fasting"),
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

NOT_IN_CARE_REASONS = (
    ("transferred", "Transferred"),
    (LOST_TO_FOLLOWUP, "Lost to followup"),
    (OTHER, "Other, please specify..."),
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

NEW_DIAGNOSES = (
    (NONE, "No new diagnoses to report"),
    (DIABETES, "Diabetes"),
    (HYPERTENSION, "Hypertension"),
    (OTHER, "Other reportable diagnosis ..."),
)

MEDICATION_CHANGES = (
    (NONE, "No medication changes to report"),
    (DIABETES, "Diabetes medication has changed"),
    (HYPERTENSION, "Hypertension medication has changed"),
    (OTHER, "Other reportable medications have changed ..."),
)

MEDICATION_CODES = (
    (INITIAL, "Initial"),
    (MODIFIED, "Modified"),
    (HELD, "Held"),
    (STOPPED, "Stopped"),
)
