from edc_visit_schedule import FormsCollection, Requisition
from mapitio_labs import (
    blood_glucose_panel,
    blood_glucose_poc_panel,
    hba1c_panel,
    hba1c_poc_panel,
)

requisitions_prn = FormsCollection(
    Requisition(
        show_order=10, panel=blood_glucose_panel, required=True, additional=False
    ),
    Requisition(
        show_order=20, panel=blood_glucose_poc_panel, required=True, additional=False
    ),
    Requisition(show_order=30, panel=hba1c_poc_panel, required=True, additional=False),
    Requisition(show_order=40, panel=hba1c_panel, required=True, additional=False),
    name="requisitions_prn",
)

requisitions_d1 = FormsCollection(name="requisitions_day1",)
requisitions_1m = FormsCollection(name="requisitions_1m",)
requisitions_2m = FormsCollection(name="requisitions_2m",)
requisitions_3m = FormsCollection(name="requisitions_3m",)
requisitions_4m = FormsCollection(name="requisitions_4m",)
requisitions_5m = FormsCollection(name="requisitions_5m",)
requisitions_6m = FormsCollection(name="requisitions_6m",)
requisitions_7m = FormsCollection(name="requisitions_7m",)
requisitions_8m = FormsCollection(name="requisitions_8m",)
requisitions_9m = FormsCollection(name="requisitions_9m",)
requisitions_10m = FormsCollection(name="requisitions_10m",)
requisitions_11m = FormsCollection(name="requisitions_11m",)
requisitions_12m = FormsCollection(name="requisitions_month12",)
