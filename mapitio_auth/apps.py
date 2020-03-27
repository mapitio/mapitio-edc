from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = "mapitio_auth"
    verbose_name = "Mapitio Authentication and Permissions"
