from django.test import TestCase, tag

from ..visit_schedules.schedule import schedule
from ..visit_schedules.visit_schedule import visit_schedule


class TestVisitSchedule(TestCase):
    def test_visit_schedule_models(self):
        self.assertEqual(visit_schedule.death_report_model, "mapitio_ae.deathreport")
        self.assertEqual(visit_schedule.offstudy_model, "edc_offstudy.subjectoffstudy")
        self.assertEqual(visit_schedule.locator_model, "edc_locator.subjectlocator")

    def test_schedule_hiv_models(self):
        self.assertEqual(schedule.onschedule_model, "mapitio_prn.onschedulehiv")
        self.assertEqual(schedule.offschedule_model, "mapitio_prn.endofstudy")
        self.assertEqual(schedule.consent_model, "mapitio_consent.subjectconsent")
        self.assertEqual(schedule.appointment_model, "edc_appointment.appointment")

    def test_visit_codes_hiv(self):
        self.assertEqual(
            ["1000", "1030", "1060", "1090", "1120"],
            [visit for visit in schedule.visits],
        )

    def test_visit_codes_ncd(self):
        self.assertEqual(
            [
                "1000",
                "1010",
                "1030",
                "1040",
                "1050",
                "1060",
                "1070",
                "1080",
                "1090",
                "1100",
                "1110",
                "1120",
            ],
            [visit for visit in schedule_ncd.visits],
        )

    def test_crfs(self):
        prn = [
            "mapitio_subject.bloodresultsfbc",
            "mapitio_subject.bloodresultsglu",
            "mapitio_subject.bloodresultshba1c",
            "mapitio_subject.bloodresultslft",
            "mapitio_subject.bloodresultsrft",
            "mapitio_subject.urinedipsticktest",
        ]
        expected = {
            "1000": [
                "mapitio_subject.physicalexam",
                "mapitio_subject.patienthistory",
                "mapitio_subject.bloodresultsfbc",
                "mapitio_subject.bloodresultslft",
                "mapitio_subject.bloodresultsrft",
                "mapitio_subject.urinedipsticktest",
            ],
            "1005": [
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.healtheconomics",
                "mapitio_subject.medicationadherence",
            ],
            "1010": [
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.medicationadherence",
            ],
            "1030": [
                "mapitio_subject.bloodresultslft",
                "mapitio_subject.bloodresultsrft",
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.medicationadherence",
            ],
            "1060": [
                "mapitio_subject.bloodresultshba1c",
                "mapitio_subject.bloodresultslft",
                "mapitio_subject.bloodresultsrft",
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.medicationadherence",
            ],
            "1090": [
                "mapitio_subject.bloodresultslft",
                "mapitio_subject.bloodresultsrft",
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.medicationadherence",
            ],
            "1120": [
                "mapitio_subject.bloodresultsfbc",
                "mapitio_subject.bloodresultsglu",
                "mapitio_subject.bloodresultshba1c",
                "mapitio_subject.bloodresultslft",
                "mapitio_subject.bloodresultsrft",
                "mapitio_subject.followupvitals",
                "mapitio_subject.followup",
                "mapitio_subject.medicationadherence",
                "mapitio_subject.urinedipsticktest",
            ],
        }
        for visit_code, visit in schedule_hiv.visits.items():
            actual = [crf.model for crf in visit.crfs]
            actual.sort()
            expected.get(visit_code).sort()
            self.assertEqual(
                expected.get(visit_code), actual, msg=f"see CRFs for visit {visit_code}"
            )

            actual = [crf.model for crf in visit.crfs_prn]
            actual.sort()
            self.assertEqual(prn, actual, msg=f"see PRN CRFs for visit {visit_code}")
