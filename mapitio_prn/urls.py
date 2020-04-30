from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import mapitio_prn_admin

app_name = "mapitio_prn"

urlpatterns = [
    path("admin/", mapitio_prn_admin.urls),
    path("", RedirectView.as_view(url=f"/{app_name}/admin/"), name="home_url"),
]
