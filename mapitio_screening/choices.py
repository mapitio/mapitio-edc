from edc_constants.constants import OTHER

from .constants import NCD_CLINIC, HIV_CLINIC

CLINIC_CHOICES = (
    (HIV_CLINIC, "HIV Clinic"),
    (NCD_CLINIC, "NCD Clinic"),
)

REFUSAL_REASONS = (
    ("unwilling_to_say", "I am unwilling to say"),
    ("dont_have_time", "I don't have time"),
    ("stigma", "I am worried about stigma"),
    ("must_consult_spouse", "I need to consult my spouse"),
    ("dont_want_medication", "I don't want to take any more medication"),
    ("dont_want_to_join", "I don't want to take part"),
    ("need_to_think_about_it", "I haven't had a chance to think about it"),
    ("moving", "I am moving to another area"),
    (OTHER, "Other, please specify"),
)
