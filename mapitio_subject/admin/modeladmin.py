from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import (
    ModelAdminSubjectDashboardMixin,
    ModelAdminCrfDashboardMixin,
)


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(ModelAdminCrfDashboardMixin):
    def get_list_display(self, request):
        super().get_list_display(request)
        if "crf_status" not in self.list_display:
            self.list_display = list(self.list_display)
            self.list_display.append("crf_status")
        return self.list_display

    def get_list_filter(self, request):
        super().get_list_filter(request)
        if "crf_status" not in self.list_filter:
            self.list_filter = list(self.list_filter)
            self.list_filter.insert(0, "crf_status")
        return self.list_filter


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):

    pass
