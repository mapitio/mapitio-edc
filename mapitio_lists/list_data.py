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
        (OTHER, ("Other reason (specify below)"),),
    ],
    "mapitio_lists.hypertensiontreatment": [
        ("thiazide_diuretics", "Thiazide diuretics"),
        ("angiotensin_2", "Angiotensin 2 Receptor Blocker"),
        ("ace_inhibitor", "ACE inhibitor"),
        ("beta_blocker", "Beta blocker"),
        ("calcium_channel_blocker", "Calcium channel blocker"),
        (NOT_APPLICABLE, "Not applicable"),
        (UNKNOWN, "Unknown"),
        (OTHER, "Other treatment (specify below)"),
    ],
    "mapitio_lists.arvregimens": [
        ("ABC_3TC/FTC", "ABC + 3TC/FTC"),
        ("AZT_FTC/3TC", "AZT + FTC/3TC"),
        ("TDF_FTC/3TC", "TDF + FTC/3TC"),
        ("ATV_r", "ATV/r"),
        ("DRV_r", "DRV/r"),
        ("DTG", "DTG"),
        ("EFV", "EFV"),
        ("Lopinavir_r", "Lopinavir/r"),
        ("NVP", "NVP"),
        (NOT_APPLICABLE, "Not applicable"),
        (UNKNOWN, "Unknown"),
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
        (OTHER, "Other, specify"),
    ],
}


if settings.APP_NAME != "mapitio_lists":
    preload_data = PreloadData(list_data=list_data)
