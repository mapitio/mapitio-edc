from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import mapitio_export_admin

app_name = "mapitio_export"

urlpatterns = [
    path("admin/", mapitio_export_admin.urls),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
]
