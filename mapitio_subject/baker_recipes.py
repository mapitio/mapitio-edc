from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_consent.constants import HOSPITAL_NUMBER
from edc_constants.constants import YES, NO, COMPLETE
from edc_utils import get_utcnow
from mapitio_subject.models import (
    DiabetesReview,
    Enrolment,
    BasicIndicators,
    BloodResults,
    HivReview,
    HypertensionReview,
    Investigations,
)
from model_bakery import seq
from model_bakery.recipe import Recipe
from faker import Faker


fake = Faker()

enrollment = Recipe(
    Enrolment,
    site=Site.objects.get_current,
    enrollment_identifier=None,
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

basicindicators = Recipe(BasicIndicators, crf_status=COMPLETE)
bloodresults = Recipe(BloodResults, crf_status=COMPLETE)
medications = Recipe(HivReview, crf_status=COMPLETE)
investigations = Recipe(Investigations, crf_status=COMPLETE)
diabetesreview = Recipe(DiabetesReview, crf_status=COMPLETE)
hypertensionreview = Recipe(HypertensionReview, crf_status=COMPLETE)
