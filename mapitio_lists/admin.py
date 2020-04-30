from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin

from .admin_site import mapitio_lists_admin
from .models import (
    ArvRegimens,
    ChestXrayFindings,
    CholesterolMedications,
    Conditions,
    DiabetesMedications,
    Diagnoses,
    EcgFindings,
    EchoFindings,
    HypertensionMedications,
    OffstudyReasons,
    VisitReasons,
)


@admin.register(EcgFindings, site=mapitio_lists_admin)
class EcgFindingsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(EchoFindings, site=mapitio_lists_admin)
class EchoFindingsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Diagnoses, site=mapitio_lists_admin)
class DiagnosesAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(CholesterolMedications, site=mapitio_lists_admin)
class CholesterolMedicationsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ChestXrayFindings, site=mapitio_lists_admin)
class ChestXrayFindingsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Conditions, site=mapitio_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=mapitio_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HypertensionMedications, site=mapitio_lists_admin)
class HypertensionMedicationsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ArvRegimens, site=mapitio_lists_admin)
class ArvRegimensAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(VisitReasons, site=mapitio_lists_admin)
class VisitReasonsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(DiabetesMedications, site=mapitio_lists_admin)
class DiabetesMedicationsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass
