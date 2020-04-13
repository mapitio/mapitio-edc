from django.test import TestCase, tag
from model_bakery.baker import make_recipe


class TestEnrolment(TestCase):
    @tag("1")
    def test_(self):
        enrolment = make_recipe("mapitio_subject.enrolment")
