from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


class AdminSite(DjangoAdminSite):
    site_title = "MAPITIO: Subject CRFs"
    site_header = "MAPITIO: Subject CRFs"
    index_title = "MAPITIO: Subject CRFs"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        label = f"Mapitio {get_current_site(request).name.title()}: Subject CRFs"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


mapitio_subject_admin = AdminSite(name="mapitio_subject_admin")
mapitio_subject_admin.disable_action("delete_selected")
