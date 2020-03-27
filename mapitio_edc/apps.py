from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_edc"


class AppConfigForTests(DjangoAppConfig):
    name = "mapitio_edc"
