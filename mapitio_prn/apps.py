from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_prn"
    verbose_name = "Mapitio: PRN Forms"
    include_in_administration_section = True
    has_exportable_data = True
