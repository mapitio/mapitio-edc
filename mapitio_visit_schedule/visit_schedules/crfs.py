from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=200, model="mapitio_subject.deathreport", required=False),
    name="prn",
)

crfs_d1 = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.indicators"),
    Crf(show_order=110, model="mapitio_subject.hivhistory"),
    Crf(show_order=120, model="mapitio_subject.ncdhistory"),
    Crf(show_order=130, model="mapitio_subject.biomedicalhistory"),
    Crf(show_order=140, model="mapitio_subject.followup"),
    # Crf(show_order=150, model="mapitio_subject.deathreport", required=False),
    Crf(show_order=160, model="mapitio_subject.ncdfollowup"),
    Crf(show_order=170, model="mapitio_subject.biomedicalfollowup"),
    Crf(show_order=180, model="mapitio_subject.complications"),
    Crf(show_order=190, model="mapitio_subject.investigations"),
    name="day1",
)
