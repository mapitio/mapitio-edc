from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_subject"
    verbose_name = "Mapitio: Subject"
    include_in_administration_section = True
    has_exportable_data = True
