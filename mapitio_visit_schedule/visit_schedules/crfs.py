from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(name="prn",)

crfs_d1 = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.enrollment"),
    Crf(show_order=110, model="mapitio_subject.hivhistory"),
    Crf(show_order=120, model="mapitio_subject.ncdhistory"),
    Crf(show_order=130, model="mapitio_subject.baselinedata"),
    Crf(show_order=140, model="mapitio_subject.bloodresults"),
    Crf(show_order=150, model="mapitio_subject.investigations"),
    Crf(show_order=160, model="mapitio_subject.followup"),
    name="day1",
)
crfs_1m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="1m"
)
crfs_2m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="2m"
)
crfs_3m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="3m"
)
crfs_4m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="4m"
)
crfs_5m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="5m"
)
crfs_6m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="6m",
)
crfs_7m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="7m"
)
crfs_8m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="8m"
)
crfs_9m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="9m"
)
crfs_10m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="10m"
)
crfs_11m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="11m"
)
crfs_12m = FormsCollection(
    Crf(show_order=100, model="mapitio_subject.followup"), name="12m",
)
