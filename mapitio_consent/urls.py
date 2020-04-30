from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import mapitio_consent_admin

app_name = "mapitio_consent"

urlpatterns = [
    path("admin/", mapitio_consent_admin.urls),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
]
