from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from .admin_site import mapitio_lists_admin
from .models import (
    Conditions,
    OffstudyReasons,
    HypertensionTreatment,
    DiabetesTreatment,
    VisitReasons,
    ArvRegimens,
)


@admin.register(Conditions, site=mapitio_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=mapitio_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HypertensionTreatment, site=mapitio_lists_admin)
class HypertensionTreatmentAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ArvRegimens, site=mapitio_lists_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(VisitReasons, site=mapitio_lists_admin)
class VisitReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(DiabetesTreatment, site=mapitio_lists_admin)
class DiabetesTreatmentAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
