from edc_auth import (
    AUDITOR,
    CLINIC,
    DATA_MANAGER,
    SCREENING,
    UNBLINDING_REQUESTORS,
    UNBLINDING_REVIEWERS,
    data_manager,
    get_default_codenames_by_group,
)

from django.conf import settings
from .codenames import (
    auditor,
    clinic,
    screening,
    unblinding_requestors,
    unblinding_reviewers,
)


def get_codenames_by_group():
    codenames_by_group = {k: v for k, v in get_default_codenames_by_group().items()}
    codenames_by_group[AUDITOR] = auditor
    codenames_by_group[CLINIC] = clinic
    codenames_by_group[SCREENING] = screening
    codenames_by_group[UNBLINDING_REQUESTORS] = unblinding_requestors
    codenames_by_group[UNBLINDING_REVIEWERS] = unblinding_reviewers
    codenames_by_group[DATA_MANAGER] = data_manager

    # remove all refs to SCREENING
    if settings.MAPITIO_SCREENING_DISABLED:
        for group_name, codenames in codenames_by_group.items():
            for codename in codenames:
                if "screening" in codename:
                    codenames.remove(codename)
    return codenames_by_group
