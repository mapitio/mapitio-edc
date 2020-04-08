from django.conf import settings
from edc_auth.codenames import clinic


clinic += [
    "mapitio_lists.view_arvregimens",
    "mapitio_lists.view_conditions",
    "mapitio_lists.view_diabetestreatment",
    "mapitio_lists.view_hypertensiontreatment",
    "mapitio_lists.view_offstudyreasons",
    "mapitio_prn.add_endofstudy",
    "mapitio_prn.add_losstofollowup",
    "mapitio_prn.add_onschedule",
    "mapitio_prn.add_protocoldeviationviolation",
    "mapitio_prn.change_endofstudy",
    "mapitio_prn.change_losstofollowup",
    "mapitio_prn.change_onschedule",
    "mapitio_prn.change_protocoldeviationviolation",
    "mapitio_prn.delete_endofstudy",
    "mapitio_prn.delete_losstofollowup",
    "mapitio_prn.delete_onschedule",
    "mapitio_prn.delete_protocoldeviationviolation",
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
    "mapitio_subject.add_bloodresults",
    "mapitio_subject.add_baselinedata",
    "mapitio_subject.add_followup",
    "mapitio_subject.add_enrolment",
    "mapitio_subject.add_hivhistory",
    "mapitio_subject.add_investigations",
    "mapitio_subject.add_ncdhistory",
    "mapitio_subject.add_subjectrequisition",
    "mapitio_subject.add_subjectvisit",
    "mapitio_subject.change_bloodresults",
    "mapitio_subject.change_baselinedata",
    "mapitio_subject.change_followup",
    "mapitio_subject.change_enrolment",
    "mapitio_subject.change_hivhistory",
    "mapitio_subject.change_investigations",
    "mapitio_subject.change_ncdhistory",
    "mapitio_subject.change_subjectrequisition",
    "mapitio_subject.change_subjectvisit",
    "mapitio_subject.delete_bloodresults",
    "mapitio_subject.delete_baselinedata",
    "mapitio_subject.delete_followup",
    "mapitio_subject.delete_enrolment",
    "mapitio_subject.delete_hivhistory",
    "mapitio_subject.delete_investigations",
    "mapitio_subject.delete_ncdhistory",
    "mapitio_subject.delete_subjectrequisition",
    "mapitio_subject.delete_subjectvisit",
    "mapitio_subject.view_bloodresults",
    "mapitio_subject.view_baselinedata",
    "mapitio_subject.view_followup",
    "mapitio_subject.view_enrolment",
    "mapitio_subject.view_historicalbloodresults",
    "mapitio_subject.view_historicalbaselinedata",
    "mapitio_subject.view_historicalfollowup",
    "mapitio_subject.view_historicalenrolment",
    "mapitio_subject.view_historicalhivhistory",
    "mapitio_subject.view_historicalinvestigations",
    "mapitio_subject.view_historicalncdhistory",
    "mapitio_subject.view_historicalsubjectrequisition",
    "mapitio_subject.view_historicalsubjectvisit",
    "mapitio_subject.view_hivhistory",
    "mapitio_subject.view_investigations",
    "mapitio_subject.view_ncdhistory",
    "mapitio_subject.view_subjectrequisition",
    "mapitio_subject.view_subjectvisit",
]
clinic.sort()