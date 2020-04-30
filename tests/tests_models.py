# from django.test import TestCase, tag
# from edc_registration.models import RegisteredSubject
# from edc_sites import add_or_update_django_sites
# from edc_visit_schedule.constants import DAY1
# from mapitio_consent.models import SubjectConsent
# from mapitio_screening.models import SubjectScreening
# from mapitio_subject.models import (
#     Indicators,
#     BiomedicalHistory,
#     Investigations,
#     HivReview,
#     HypertensionReview,
# )
# from model_bakery.baker import make_recipe
#
# from django.core.exceptions import ObjectDoesNotExist
# from faker import Faker
# from .mapitio_test_case import MapitioTestCaseMixin
#
# fake = Faker()
#
#
# class TestMapitio(MapitioTestCaseMixin, TestCase):
#     def setUp(self):
#         all_sites = add_or_update_django_sites()
#         self.assertIn("tanzania", all_sites)
#
#     def test_enrollment(self):
#         enrollment = make_recipe("mapitio_subject.enrollment")
#         self.assertEqual(enrollment.age_in_years, 25)
#         enrollment.refresh_from_db()
#         screening = SubjectScreening.objects.get(
#             enrollment_identifier=enrollment.enrollment_identifier
#         )
#         enrollment.refresh_from_db()
#
#         # assert RegisteredSubject  exists
#         try:
#             rs = RegisteredSubject.objects.get(
#                 screening_identifier=screening.screening_identifier
#             )
#         except ObjectDoesNotExist:
#             self.fail("RegisteredSubject record unexpectedly does not exist")
#
#         # assert subject identifier format, e.g is not UUID
#         self.assertRegexpMatches(rs.subject_identifier, "[0-9\-]+")
#
#         # assert all have subject identifier
#         consent = SubjectConsent.objects.get(
#             screening_identifier=screening.screening_identifier
#         )
#         self.assertEqual(enrollment.subject_identifier, rs.subject_identifier)
#         self.assertEqual(screening.subject_identifier, rs.subject_identifier)
#         self.assertEqual(consent.subject_identifier, rs.subject_identifier)
#
#     def test_baseline(self):
#         enrollment = make_recipe("mapitio_subject.enrollment")
#         enrollment.refresh_from_db()
#         subject_visit = self.get_subject_visit(visit_code=DAY1, enrollment=enrollment)
#         self.assertRegexpMatches(subject_visit.subject_identifier, "[0-9\-]+")
#
#         basic_indicators = make_recipe(
#             "mapitio_subject.indicators", subject_visit=subject_visit
#         )
#         basic_indicators.save()
#         self.assertGreater(Indicators.history.all().count(), 0)
#         blood_results = make_recipe(
#             "mapitio_subject.bloodresults", subject_visit=subject_visit
#         )
#         blood_results.save()
#         self.assertGreater(BloodResults.history.all().count(), 0)
#
#         hiv_review = make_recipe(
#             "mapitio_subject.hivhistory", subject_visit=subject_visit
#         )
#         hiv_review.save()
#         self.assertGreater(HivReview.history.all().count(), 0)
#
#         investigations = make_recipe(
#             "mapitio_subject.investigations", subject_visit=subject_visit
#         )
#         investigations.save()
#         self.assertGreater(Investigations.history.all().count(), 0)
#
#         hypertension_review = make_recipe(
#             "mapitio_subject.hypertensionreview", subject_visit=subject_visit
#         )
#         hypertension_review.save()
#         self.assertGreater(HypertensionReview.history.all().count(), 0)
#
#         diabetes_review = make_recipe(
#             "mapitio_subject.diabetesreview", subject_visit=subject_visit
#         )
#         diabetes_review.save()
#         self.assertGreater(DiabetesReview.history.all().count(), 0)
