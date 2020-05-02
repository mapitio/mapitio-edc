from django.conf import settings
from edc_auth.codenames import auditor

auditor += [
    "mapitio_lists.view_arvregimens",
    "mapitio_lists.view_chestxrayfindings",
    "mapitio_lists.view_cholesterolmedications",
    "mapitio_lists.view_conditions",
    "mapitio_lists.view_diabetesmedications",
    "mapitio_lists.view_ecgfindings",
    "mapitio_lists.view_echofindings",
    "mapitio_lists.view_hypertensionmedications",
    "mapitio_lists.view_offstudyreasons",
    "mapitio_prn.view_endofstudy",
    "mapitio_prn.view_historicalendofstudy",
    "mapitio_prn.view_historicallosstofollowup",
    "mapitio_prn.view_historicalonschedule",
    "mapitio_prn.view_historicalprotocoldeviationviolation",
    "mapitio_prn.view_losstofollowup",
    "mapitio_prn.view_onschedule",
    "mapitio_prn.view_protocoldeviationviolation",
    "mapitio_prn.view_unblindingrequestoruser",
    "mapitio_prn.view_unblindingrevieweruser",
    "mapitio_subject.view_biomedicalhistory",
    "mapitio_subject.view_biomedicalfollowup",
    "mapitio_subject.view_complications",
    "mapitio_subject.view_deathreport",
    "mapitio_subject.view_followup",
    "mapitio_subject.view_historicalbiomedicalhistory",
    "mapitio_subject.view_historicalbiomedicalfollowup",
    "mapitio_subject.view_historicalcomplications",
    "mapitio_subject.view_historicaldeathreport",
    "mapitio_subject.view_historicalfollowup",
    "mapitio_subject.view_historicalhivhistory",
    "mapitio_subject.view_historicalindicators",
    "mapitio_subject.view_historicalinvestigations",
    "mapitio_subject.view_historicalncdfollowup",
    "mapitio_subject.view_historicalncdhistory",
    "mapitio_subject.view_historicalsubjectrequisition",
    "mapitio_subject.view_historicalsubjectvisit",
    "mapitio_subject.view_hivhistory",
    "mapitio_subject.view_indicators",
    "mapitio_subject.view_investigations",
    "mapitio_subject.view_ncdfollowup",
    "mapitio_subject.view_ncdhistory",
    "mapitio_subject.view_subjectrequisition",
    "mapitio_subject.view_subjectvisit",
]

if settings.MAPITIO_SCREENING_DISABLED:
    for item in auditor:
        if "screening" in item:
            auditor.remove(item)
auditor.sort()
