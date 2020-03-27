from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_ae"
    verbose_name = "Mapitio: Adverse Events"
    include_in_administration_section = True
    has_exportable_data = True
