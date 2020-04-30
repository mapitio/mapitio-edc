from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "mapitio_lists"
    verbose_name = "Mapitio: Lists"
    include_in_administration_section = True
    has_exportable_data = True
