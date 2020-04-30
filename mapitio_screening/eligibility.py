from django.utils.safestring import mark_safe
from edc_constants.constants import YES, TBD
from edc_utils.date import get_utcnow


class SubjectScreeningEligibilityError(Exception):
    pass


def check_eligible_final(obj):
    """Updates model instance fields `eligible` and `reasons_ineligible`.
    """
    obj.eligible = True
    obj.reasons_ineligible = None
    obj.eligibility_datetime = get_utcnow()


def calculate_eligible_final(obj):
    """Returns YES, NO or TBD.
    """
    return YES


def format_reasons_ineligible(*str_values):
    reasons = None
    str_values = [x for x in str_values if x is not None]
    if str_values:
        str_values = "".join(str_values)
        reasons = mark_safe(str_values.replace("|", "<BR>"))
    return reasons


def eligibility_display_label(obj):
    return "ELIGIBLE"
