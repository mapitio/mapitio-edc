from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):

    site_title = "Mapitio Export"
    site_header = "Mapitio Export"
    index_title = "Mapitio Export"
    site_url = "/administration/"


mapitio_export_admin = AdminSite(name="mapitio_export_admin")
