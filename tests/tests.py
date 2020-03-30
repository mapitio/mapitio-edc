import pdb

from django.test.testcases import TestCase
from edc_registration.models import RegisteredSubject
from edc_sites import add_or_update_django_sites, get_sites_module
from edc_utils import get_utcnow
from edc_visit_schedule import site_visit_schedules
from edc_visit_schedule.constants import DAY1
from mapitio_consent.models import SubjectConsent
from mapitio_screening.models import SubjectScreening
from mapitio_subject.models import Enrolment
from model_bakery import seq
from model_bakery.baker import make_recipe, prepare_recipe

from django.core.exceptions import ObjectDoesNotExist
from faker import Faker
from .mapitio_test_case import MapitioTestCaseMixin

fake = Faker()


class TestMapitio(MapitioTestCaseMixin, TestCase):
    def setUp(self):
        all_sites = add_or_update_django_sites()
        self.assertIn("tanzania", all_sites)

    def test_enrolment(self):
        enrolment = make_recipe("mapitio_subject.enrolment")
        self.assertEqual(enrolment.age_in_years, 25)

        enrolment.refresh_from_db()
        screening = SubjectScreening.objects.get(
            enrolment_identifier=enrolment.enrolment_identifier
        )
        enrolment.refresh_from_db()
        try:
            rs = RegisteredSubject.objects.get(
                screening_identifier=screening.screening_identifier
            )
        except ObjectDoesNotExist:
            self.fail("RegisteredSubject record unexpectedly does not exist")

        self.assertRegexpMatches(rs.subject_identifier, "[0-9\-]+")
        print(rs.subject_identifier)
        try:
            rs = RegisteredSubject.objects.get(
                subject_identifier=screening.subject_identifier
            )
        except ObjectDoesNotExist:
            self.fail("RegisteredSubject record unexpectedly does not exist")

        self.assertEqual(enrolment.subject_identifier, rs.subject_identifier)

    def test_baseline(self):
        enrolment = make_recipe("mapitio_subject.enrolment")
        enrolment.refresh_from_db()
        subject_visit = self.get_subject_visit(visit_code=DAY1, enrolment=enrolment)
        baseline_data = make_recipe(
            "mapitio_subject.baselinedata", subject_visit=subject_visit
        )
        blood_results = make_recipe(
            "mapitio_subject.bloodresults", subject_visit=subject_visit
        )
        hiv_history = make_recipe(
            "mapitio_subject.hivhistory", subject_visit=subject_visit
        )
        investigations = make_recipe(
            "mapitio_subject.investigations", subject_visit=subject_visit
        )
        ncd_history = make_recipe(
            "mapitio_subject.ncdhistory", subject_visit=subject_visit
        )
