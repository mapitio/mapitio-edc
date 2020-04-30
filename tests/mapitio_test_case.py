import pdb
from copy import copy

from django.contrib.auth.models import Group
from edc_appointment.constants import IN_PROGRESS_APPT
from edc_appointment.models import Appointment
from edc_auth.group_permissions_updater import GroupPermissionsUpdater
from edc_constants.constants import COMPLETE
from edc_facility.import_holidays import import_holidays
from edc_facility.models import Holiday
from edc_list_data.site_list_data import site_list_data
from edc_randomization.randomization_list_importer import RandomizationListImporter
from edc_sites import add_or_update_django_sites, get_sites_by_country
from edc_sites.tests.site_test_case_mixin import SiteTestCaseMixin
from edc_visit_schedule.constants import DAY1
from edc_visit_tracking.constants import SCHEDULED
from mapitio_auth.codenames_by_group import get_codenames_by_group
from mapitio_subject.forms import EnrolmentForm
from mapitio_subject.models import Enrolment, SubjectVisit
from model_bakery.baker import prepare_recipe
from mapitio_edc.sites import fqdn


class MapitioTestCaseMixin(SiteTestCaseMixin):
    fqdn = fqdn

    default_sites = get_sites_by_country("tanzania")

    site_names = [s.name for s in default_sites]

    import_randomization_list = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import_holidays(test=True)
        add_or_update_django_sites(sites=get_sites_by_country("tanzania"))
        site_list_data.autodiscover()
        GroupPermissionsUpdater(
            codenames_by_group=get_codenames_by_group(), verbose=True
        )
        if cls.import_randomization_list:
            RandomizationListImporter(verbose=False, name="default")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        Holiday.objects.all().delete()

    def login(self, user=None, superuser=None, groups=None):
        user = self.user if user is None else user
        superuser = True if superuser is None else superuser
        if not superuser:
            user.is_superuser = False
            user.is_active = True
            user.save()
            for group_name in groups:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
        return self.client.force_login(user or self.user)

    def get_subject_visit(self, visit_code=None, enrollment=None):
        visit_code = visit_code or DAY1
        subject_identifier = enrollment.subject_identifier
        appointment = Appointment.objects.get(
            subject_identifier=subject_identifier, visit_code=visit_code
        )
        appointment.appt_status = IN_PROGRESS_APPT
        appointment.save()
        return SubjectVisit.objects.create(appointment=appointment, reason=SCHEDULED)
