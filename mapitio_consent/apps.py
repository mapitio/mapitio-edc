from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_consent"
    verbose_name = "Mapitio: Consent"
    include_in_administration_section = True
    has_exportable_data = True
