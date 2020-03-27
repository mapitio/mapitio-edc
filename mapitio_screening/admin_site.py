from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):
    site_title = "Mapitio Screening CRFs"
    site_header = "Mapitio Screening CRFs"
    index_title = "Mapitio Screening CRFs"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        context.update(global_site=get_current_site(request))
        label = f"Mapitio: {title.title()} - Screening CRFs"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


mapitio_screening_admin = AdminSite(name="mapitio_screening_admin")
mapitio_screening_admin.disable_action("delete_selected")
