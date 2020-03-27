from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):
    site_title = "Mapitio PRN"
    site_header = "Mapitio PRN"
    index_title = "Mapitio PRN"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        context.update(global_site=get_current_site(request))
        label = f"INTE: {title.title()} - PRN"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


mapitio_prn_admin = AdminSite(name="mapitio_prn_admin")
mapitio_prn_admin.disable_action("delete_selected")
