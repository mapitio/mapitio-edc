from edc_constants.constants import YES
from edc_metadata import REQUIRED, NOT_REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P


@register()
class BasicIndicatorsRuleGroup(CrfRuleGroup):

    hiv = CrfRule(
        predicate=P("hiv_pos", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hivreview"],
    )

    diabetic = CrfRule(
        predicate=P("diabetic", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["diabetesreview"],
    )

    hypertensive = CrfRule(
        predicate=P("hypertensive", "eq", YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["hypertensionreview"],
    )

    class Meta:
        app_label = "inte_subject"
        source_model = "baselinedata"
