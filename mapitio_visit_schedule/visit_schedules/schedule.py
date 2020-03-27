from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit
from edc_visit_schedule.constants import (
    DAY1,
    MONTH6,
    MONTH12,
    MONTH4,
    MONTH3,
    MONTH2,
    MONTH5,
    MONTH7,
    MONTH8,
    MONTH9,
    MONTH1,
    MONTH11,
    MONTH10,
)

from .crfs import (
    crfs_d1,
    crfs_1m,
    crfs_2m,
    crfs_3m,
    crfs_4m,
    crfs_5m,
    crfs_6m,
    crfs_7m,
    crfs_8m,
    crfs_9m,
    crfs_10m,
    crfs_11m,
    crfs_12m,
    #     crfs_prn as default_crfs_prn,
    #     crfs_unscheduled as default_crfs_unscheduled,
)
from .requisitions import (
    requisitions_d1,
    requisitions_1m,
    requisitions_2m,
    requisitions_3m,
    requisitions_4m,
    requisitions_5m,
    requisitions_6m,
    requisitions_7m,
    requisitions_8m,
    requisitions_9m,
    requisitions_10m,
    requisitions_11m,
    requisitions_12m,
    #     requisitions_prn as default_requisitions_prn,
)

default_requisitions = None


class Visit(BaseVisit):
    def __init__(
        self,
        crfs_unscheduled=None,
        requisitions_unscheduled=None,
        crfs_prn=None,
        requisitions_prn=None,
        allow_unscheduled=None,
        **kwargs
    ):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,  # or default_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn,  # or default_crfs_prn,
            requisitions_prn=requisitions_prn,  # or default_requisitions_prn,
            **kwargs
        )


# schedule for new participants
schedule = Schedule(
    name="schedule",
    verbose_name="History and Follow-up",
    onschedule_model="mapitio_prn.onschedule",
    offschedule_model="mapitio_prn.endofstudy",
    consent_model="mapitio_consent.subjectconsent",
    appointment_model="edc_appointment.appointment",
)

visit00 = Visit(
    code=DAY1,
    title="Day 1",
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d1,
    crfs=crfs_d1,
    facility_name="7-day-clinic",
)

visit01 = Visit(
    code=MONTH1,
    title="Month 1",
    timepoint=1,
    rbase=relativedelta(months=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_1m,
    crfs=crfs_1m,
    facility_name="7-day-clinic",
)

visit02 = Visit(
    code=MONTH2,
    title="Month 2",
    timepoint=2,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_2m,
    crfs=crfs_2m,
    facility_name="7-day-clinic",
)

visit03 = Visit(
    code=MONTH3,
    title="Month 3",
    timepoint=3,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_3m,
    crfs=crfs_3m,
    facility_name="7-day-clinic",
)

visit04 = Visit(
    code=MONTH4,
    title="Month 4",
    timepoint=4,
    rbase=relativedelta(months=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_4m,
    crfs=crfs_4m,
    facility_name="7-day-clinic",
)

visit05 = Visit(
    code=MONTH5,
    title="Month 5",
    timepoint=5,
    rbase=relativedelta(months=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_5m,
    crfs=crfs_5m,
    facility_name="7-day-clinic",
)
visit06 = Visit(
    code=MONTH6,
    title="Month 6",
    timepoint=6,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_6m,
    crfs=crfs_6m,
    facility_name="7-day-clinic",
)

visit07 = Visit(
    code=MONTH7,
    title="Month 7",
    timepoint=7,
    rbase=relativedelta(months=7),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_7m,
    crfs=crfs_7m,
    facility_name="7-day-clinic",
)

visit08 = Visit(
    code=MONTH8,
    title="Month 8",
    timepoint=8,
    rbase=relativedelta(months=8),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_8m,
    crfs=crfs_8m,
    facility_name="7-day-clinic",
)

visit09 = Visit(
    code=MONTH9,
    title="Month 9",
    timepoint=9,
    rbase=relativedelta(months=9),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_9m,
    crfs=crfs_9m,
    facility_name="7-day-clinic",
)

visit10 = Visit(
    code=MONTH10,
    title="Month 10",
    timepoint=10,
    rbase=relativedelta(months=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_10m,
    crfs=crfs_10m,
    facility_name="7-day-clinic",
)

visit11 = Visit(
    code=MONTH11,
    title="Month 11",
    timepoint=11,
    rbase=relativedelta(months=11),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_11m,
    crfs=crfs_11m,
    facility_name="7-day-clinic",
)

visit12 = Visit(
    code=MONTH12,
    title="Month 12",
    timepoint=12,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_12m,
    crfs=crfs_12m,
    facility_name="7-day-clinic",
)

schedule.add_visit(visit=visit00)
schedule.add_visit(visit=visit01)
schedule.add_visit(visit=visit02)
schedule.add_visit(visit=visit03)
schedule.add_visit(visit=visit04)
schedule.add_visit(visit=visit05)
schedule.add_visit(visit=visit06)
schedule.add_visit(visit=visit07)
schedule.add_visit(visit=visit08)
schedule.add_visit(visit=visit09)
schedule.add_visit(visit=visit10)
schedule.add_visit(visit=visit11)
schedule.add_visit(visit=visit12)
