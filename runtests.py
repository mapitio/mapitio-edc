#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join

from edc_utils import get_datetime_from_env
from multisite import SiteID

app_name = "mapitio_edc"
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SITE_ID=SiteID(default=10),
    MAPITIO_SCREENING_DISABLED=True,
    EDC_SITES_MODULE_NAME="mapitio_edc.sites",
    SUBJECT_VISIT_MODEL="mapitio_subject.subjectvisit",
    SUBJECT_CONSENT_MODEL="mapitio_consent.subjectconsent",
    SUBJECT_REQUISITION_MODEL=f"mapitio_subject.subjectrequisition",
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=get_datetime_from_env(2020, 1, 30, 0, 0, 0, "UTC"),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=get_datetime_from_env(
        2024, 12, 31, 23, 59, 59, "UTC"
    ),
    ADVERSE_EVENT_ADMIN_SITE="mapitio_ae_admin",
    ADVERSE_EVENT_APP_LABEL="mapitio_ae",
    EDC_NAVBAR_DEFAULT="mapitio_dashboard",
    DASHBOARD_BASE_TEMPLATES=dict(
        edc_base_template="edc_dashboard/base.html",
        listboard_base_template="mapitio_edc/base.html",
        dashboard_base_template="mapitio_edc/base.html",
        screening_listboard_template="mapitio_dashboard/screening/listboard.html",
        subject_listboard_template="mapitio_dashboard/subject/listboard.html",
        subject_dashboard_template="mapitio_dashboard/subject/dashboard.html",
        subject_review_listboard_template="edc_review_dashboard/subject_review_listboard.html",
    ),
    ETC_DIR=os.path.join(base_dir, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    EDC_RANDOMIZATION_LIST_PATH=join(base_dir, "tests", "etc"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=True,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "multisite",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "django_extensions",
        # "django_celery_results",
        # "django_celery_beat",
        "logentry_admin",
        "simple_history",
        "storages",
        "edc_action_item.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_fieldsets.apps.AppConfig",
        "edc_form_validators.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_label.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_metadata_rules.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_model_wrapper.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_pdutils.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_reportable.apps.AppConfig",
        "edc_reports.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "mapitio_lists.apps.AppConfig",
        "mapitio_dashboard.apps.AppConfig",
        "mapitio_labs.apps.AppConfig",
        "mapitio_metadata_rules.apps.AppConfig",
        "mapitio_reference.apps.AppConfig",
        "mapitio_screening.apps.AppConfig",
        "mapitio_subject.apps.AppConfig",
        "mapitio_consent.apps.AppConfig",
        # "mapitio_form_validators.apps.AppConfig",
        "mapitio_visit_schedule.apps.AppConfig",
        "mapitio_ae.apps.AppConfig",
        "mapitio_prn.apps.AppConfig",
        "mapitio_export.apps.AppConfig",
        "mapitio_auth.apps.AppConfig",
        "mapitio_edc.apps.AppConfigForTests",
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    add_adverse_event_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = True if [t for t in sys.argv if t == "--failfast"] else False
    failures = DiscoverRunner(failfast=failfast, tags=tags).run_tests([f"tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
