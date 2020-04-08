from django.apps import AppConfig as DjangoAppConfig
from django.db.backends.signals import connection_created
from edc_utils.sqlite import activate_foreign_keys


class AppConfig(DjangoAppConfig):
    name = "mapitio_edc"

    def ready(self):
        # for sqlite only
        connection_created.connect(activate_foreign_keys)


class AppConfigForTests(DjangoAppConfig):
    name = "mapitio_edc"
