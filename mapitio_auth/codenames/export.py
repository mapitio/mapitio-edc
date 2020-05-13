from copy import copy
from edc_auth.codenames import export as default


default += [
    "mapitio_lists.export_arvregimens",
    "mapitio_lists.export_chestxrayfindings",
    "mapitio_lists.export_cholesterolmedications",
    "mapitio_lists.export_conditions",
    "mapitio_lists.export_diabetesmedications",
    "mapitio_lists.export_ecgfindings",
    "mapitio_lists.export_echofindings",
    "mapitio_lists.export_hypertensionmedications",
    "mapitio_lists.export_offstudyreasons",
    "mapitio_prn.export_endofstudy",
    "mapitio_prn.export_losstofollowup",
    "mapitio_prn.export_onschedule",
    "mapitio_prn.export_protocoldeviationviolation",
    "mapitio_screening.export_subjectscreening",
    "mapitio_screening.export_subjectrefusal",
    "mapitio_subject.export_biomedicalhistory",
    "mapitio_subject.export_biomedicalfollowup",
    "mapitio_subject.export_complications",
    "mapitio_subject.export_deathreport",
    "mapitio_subject.export_followup",
    "mapitio_subject.export_followupindicators",
    "mapitio_subject.export_hivfollowup",
    "mapitio_subject.export_hivhistory",
    "mapitio_subject.export_indicators",
    "mapitio_subject.export_investigations",
    "mapitio_subject.export_ncdfollowup",
    "mapitio_subject.export_ncdhistory",
    "mapitio_subject.export_subjectrequisition",
    "mapitio_subject.export_subjectvisit",
]

default.sort()
export = copy(default)
