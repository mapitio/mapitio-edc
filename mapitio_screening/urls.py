from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import mapitio_screening_admin

app_name = "mapitio_screening"

urlpatterns = [
    path("admin/", mapitio_screening_admin.urls),
    path("", RedirectView.as_view(url="/mapitio_screening/admin/"), name="home_url"),
]
