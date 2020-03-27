from django.urls.conf import path
from edc_adverse_event.views import AeHomeView

from .admin_site import mapitio_ae_admin

app_name = "mapitio_ae"

urlpatterns = [
    path("admin/", mapitio_ae_admin.urls),
    path("", AeHomeView.as_view(), name="home_url"),
]
