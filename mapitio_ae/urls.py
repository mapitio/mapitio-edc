from django.urls.conf import path
from edc_adverse_event.views import AeHomeView

from .admin_site import inte_ae_admin

app_name = "mapitio_ae"

urlpatterns = [
    path("admin/", inte_ae_admin.urls),
    path("", AeHomeView.as_view(), name="home_url"),
]
