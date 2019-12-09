# Create your models here.
from edc_constants.constants import NORMAL, OTHER

from .constants import LEFT_VENTRICULAR_HYPERTROPHY

ARV = (
    (1, "AZT + 3TC + NVP"),
    (2, "AZT + 3TC + EFV"),
    (3, "AZT + 3TC + DTG"),
    (4, "ABC + 3TC + EFV"),
    (5, "ABC + 3TC + DTG"),
    (6, "d4T + 3TC + NVP"),
    (7, "d4T + 3TC + EFV"),
    (8, "TDF + FTC + EFV"),
    (9, "TDF + FTC + NVP"),
    (10, "TDF + 3TC + EFV"),
    (11, "TDF + 3TC + NVP"),
    (12, "TDF + 3TC + DTG"),
    (13, "TDF + FTC + DTG"),
    (14, "TDF + 3TC + ATV/r"),
    (15, "TDF + FTC + ATV/r"),
    (16, "TDF + 3TC + LPV/r"),
    (17, "AZT + 3TC + ATV/r"),
    (18, "AZT + 3TC + LPV/r"),
    (19, "ABC + 3TC + ATV/r"),
    (20, "ABC + 3TC + LPV/r"),
    (21, "TDF + FTC + LPV/R"),
    (22, "DTG + (ABC/3TC) + ATV/r"),
)

BLOOD_SUGAR = ((1, "Fasting"), (2, "Random"))

X_RAY = (
    (1, "Normal"),
    (2, "Pneumonia"),
    (3, "PCP"),
    (4, "Cardiomegaly"),
    (5, "Pleural effusion"),
)

ECG = (
    (1, "Normal"),
    (LEFT_VENTRICULAR_HYPERTROPHY, "Left ventricular hypertrophy"),
    (3, "Ischaemic heart disease"),
    (4, "Heart arrhythmias"),
)

ECHO = (
    (NORMAL, "Normal"),
    (LEFT_VENTRICULAR_HYPERTROPHY, "Left ventricular hypertrophy"),
    ("dystolic_dysfunction", "Dystolic dysfunction"),
    ("cardiomyopathy", "Cardiomyopathy"),
    (OTHER, "Other"),
)

IN_CARE = (
    ("yes_alive_in_clinic", "Yes, alive and in care at this clinic"),
    ("yes_alive_elsewhere", "Yes, alive and in care elsewhere"),
    ("no_deceased", "No, patient died"),
)
