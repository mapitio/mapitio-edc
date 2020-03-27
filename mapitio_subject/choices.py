from edc_constants.constants import FASTING, NON_FASTING, NORMAL, OTHER

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
