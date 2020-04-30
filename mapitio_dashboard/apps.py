from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_dashboard"
    admin_site_name = "mapitio_test_admin"
    include_in_administration_section = False
