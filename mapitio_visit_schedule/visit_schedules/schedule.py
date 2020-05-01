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

from .crfs import crfs_d1, crfs_prn
from .requisitions import requisitions_d1

default_requisitions = None


class Visit(BaseVisit):
    def __init__(
        self,
        crfs_unscheduled=None,
        requisitions_unscheduled=None,
        crfs_prn=crfs_prn,
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


schedule.add_visit(visit=visit00)
