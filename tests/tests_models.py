import pdb

from django.test import TestCase, tag
from edc_registration.models import RegisteredSubject
from edc_sites import add_or_update_django_sites
from edc_visit_schedule.constants import DAY1
from mapitio_consent.models import SubjectConsent
from mapitio_screening.models import SubjectScreening
from mapitio_subject.models import (
    BaselineData,
    BloodResults,
    Investigations,
    HivHistory,
    NcdHistory,
)
from model_bakery.baker import make_recipe

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

        # assert RegisteredSubject  exists
        try:
            rs = RegisteredSubject.objects.get(
                screening_identifier=screening.screening_identifier
            )
        except ObjectDoesNotExist:
            self.fail("RegisteredSubject record unexpectedly does not exist")

        # assert subject identifier format, e.g is not UUID
        self.assertRegexpMatches(rs.subject_identifier, "[0-9\-]+")

        # assert all have subject identifier
        consent = SubjectConsent.objects.get(
            screening_identifier=screening.screening_identifier
        )
        self.assertEqual(enrolment.subject_identifier, rs.subject_identifier)
        self.assertEqual(screening.subject_identifier, rs.subject_identifier)
        self.assertEqual(consent.subject_identifier, rs.subject_identifier)

    def test_baseline(self):
        enrolment = make_recipe("mapitio_subject.enrolment")
        enrolment.refresh_from_db()
        subject_visit = self.get_subject_visit(visit_code=DAY1, enrolment=enrolment)
        self.assertRegexpMatches(subject_visit.subject_identifier, "[0-9\-]+")

        baseline_data = make_recipe(
            "mapitio_subject.baselinedata", subject_visit=subject_visit
        )
        baseline_data.save()
        self.assertGreater(0, BaselineData.history.all().count())
        blood_results = make_recipe(
            "mapitio_subject.bloodresults", subject_visit=subject_visit
        )
        blood_results.save()
        self.assertGreater(0, BloodResults.history.all().count())
        hiv_history = make_recipe(
            "mapitio_subject.hivhistory", subject_visit=subject_visit
        )
        hiv_history.save()
        self.assertGreater(0, HivHistory.history.all().count())
        investigations = make_recipe(
            "mapitio_subject.investigations", subject_visit=subject_visit
        )
        investigations.save()
        self.assertGreater(0, Investigations.history.all().count())
        ncd_history = make_recipe(
            "mapitio_subject.ncdhistory", subject_visit=subject_visit
        )
        ncd_history.save()
        self.assertGreater(0, NcdHistory.history.all().count())
