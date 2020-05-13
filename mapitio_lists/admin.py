from django.contrib import admin
from edc_list_data.admin import ListModelAdminMixin
from import_export.admin import ExportActionMixin

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
class EcgFindingsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(EchoFindings, site=mapitio_lists_admin)
class EchoFindingsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(Diagnoses, site=mapitio_lists_admin)
class DiagnosesAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(CholesterolMedications, site=mapitio_lists_admin)
class CholesterolMedicationsAdmin(
    ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin
):
    pass


@admin.register(ChestXrayFindings, site=mapitio_lists_admin)
class ChestXrayFindingsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(Conditions, site=mapitio_lists_admin)
class ConditionsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(OffstudyReasons, site=mapitio_lists_admin)
class OffstudyReasonsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(HypertensionMedications, site=mapitio_lists_admin)
class HypertensionMedicationsAdmin(
    ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin
):
    pass


@admin.register(ArvRegimens, site=mapitio_lists_admin)
class ArvRegimensAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(VisitReasons, site=mapitio_lists_admin)
class VisitReasonsAdmin(ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(DiabetesMedications, site=mapitio_lists_admin)
class DiabetesMedicationsAdmin(
    ListModelAdminMixin, ExportActionMixin, admin.ModelAdmin
):
    pass
