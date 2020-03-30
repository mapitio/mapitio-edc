from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_consent.constants import HOSPITAL_NUMBER
from edc_constants.constants import YES, NO, COMPLETE
from edc_utils import get_utcnow
from mapitio_subject.models import (
    Enrolment,
    BaselineData,
    BloodResults,
    HivHistory,
    Investigations,
    NcdHistory,
)
from model_bakery import seq
from model_bakery.recipe import Recipe
from faker import Faker


fake = Faker()

enrolment = Recipe(
    Enrolment,
    site=Site.objects.get_current,
    enrolment_identifier=None,
    subject_identifier=None,
    report_datetime=get_utcnow(),
    first_name="OLIVER",
    last_name="MTUKUDZI",
    initials="OM",
    dob=get_utcnow().date() - relativedelta(years=25),
    is_dob_estimated=NO,
    gender="M",
    identity=seq("12315678"),
    confirm_identity=seq("12315678"),
    identity_type=HOSPITAL_NUMBER,
    crf_status=COMPLETE,
    user_created="erikvw",
)

baselinedata = Recipe(BaselineData, crf_status=COMPLETE)
bloodresults = Recipe(BloodResults, crf_status=COMPLETE)
hivhistory = Recipe(HivHistory, crf_status=COMPLETE)
investigations = Recipe(Investigations, crf_status=COMPLETE)
ncdhistory = Recipe(NcdHistory, crf_status=COMPLETE)
