from django.conf import settings
from edc_constants.constants import OTHER, UNKNOWN, DEAD, NONE, NOT_APPLICABLE
from edc_list_data import PreloadData
from mapitio_prn.constants import (
    WITHDRAWAL,
    TRANSFERRED,
    LATE_EXCLUSION,
    OTHER_RX_DISCONTINUATION,
)

list_data = {
    "mapitio_lists.conditions": [
        ("hypertension", "Patient has high blood pressure (Hypertension)"),
        ("diabetes", "Patient has high blood sugar (Diabetes)"),
        ("hiv_infection", "Patient has HIV infection (HIV+)"),
    ],
    "mapitio_lists.offstudyreasons": [
        ("completed_followup", "Patient completed 12 months of follow-up"),
        ("clinical_endpoint", "Patient reached a clinical endpoint"),
        ("toxicity", "Patient experienced an unacceptable toxicity"),
        (
            "mapitiorcurrent_illness",
            "Intercurrent illness which prevents further treatment",
        ),
        ("lost_to_followup", "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (
            OTHER_RX_DISCONTINUATION,
            "Other condition that justifies the discontinuation of "
            "treatment in the clinician’s opinion (specify below)",
        ),
        (OTHER, "Other reason (specify below)",),
    ],
    "mapitio_lists.hypertensiontreatment": [
        ("bendroflumethiazide", "Bendroflumethiazide"),
        ("captopril", "Captopril"),
        ("enalapril", "Enalapril"),
        ("ramipril", "Ramipril"),
        ("frusemide", "Frusemide"),
        ("losartan", "Losartan"),
        ("nifedipine", "Nifedipine"),
        ("amlodipine", "Amlodipine"),
        ("atenolol", "Atenolol"),
        ("metoprolol", "Metoprolol"),
        ("carvedilol", "Carvedilol"),
        ("valsartan", "Valsartan"),
        ("simvastatin", "Simvastatin"),
        (NOT_APPLICABLE, "Not applicable"),
        (OTHER, "Other treatment (specify below)"),
    ],
    "mapitio_lists.arvregimens": [
        ("TDF_3TC_ATV_r", "TDF + 3TC + ATV/r"),
        ("TDF_FTC_ATV_r", "TDF + FTC + ATV/r"),
        ("TDF_3TC_LPV_r", "TDF + 3TC + LPV/r"),
        ("AZT_3TC_ATV_r", "AZT + 3TC + ATV/r"),
        ("AZT_3TC_LPV_r", "AZT + 3TC + LPV/r"),
        ("ABC_3TC_ATV_r", "ABC + 3TC + ATV/r"),
        ("ABC_3TC_LPV_r", "ABC + 3TC + LPV/r"),
        ("TDF_FTC_LPV_r", "TDF + FTC + LPV/r"),
        ("DTG_ABC/3TC_ATV_r", "DTG + (ABC/3TC) + ATV/r"),
        (NOT_APPLICABLE, "Not applicable"),
        (OTHER, "Other, specify"),
    ],
    "mapitio_lists.visitreasons": [
        ("drug_refill", "Drug Refill"),
        ("clinic_review", "Clinic Review"),
        ("unwell", "Feeling unwell (self referral)"),
        ("unscheduled", "Unscheduled"),
    ],
    "mapitio_lists.diabetestreatment": [
        ("metformin_b", "Metformin (B)"),
        ("glibenclamide_s", "Glibenclamide (S)"),
        ("glimepiride_s", "Glimepiride (S)"),
        ("gliclazide_s", "Gliclazide (S)"),
        ("glipizide_s", "Glipizide (S)"),
        ("insulin", "Insulin"),
        (NOT_APPLICABLE, "Not applicable"),
        (OTHER, "Other, specify"),
    ],
}


if settings.APP_NAME != "mapitio_lists":
    preload_data = PreloadData(list_data=list_data)
