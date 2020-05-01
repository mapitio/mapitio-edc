from edc_constants.constants import NO, YES
from edc_metadata import REQUIRED, NOT_REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P


@register()
class FollowupRuleGroup(CrfRuleGroup):

    death_report = CrfRule(
        predicate=P("alive", "eq", NO),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=["deathreport"],
    )

    class Meta:
        app_label = "mapitio_subject"
        source_model = "followup"
