import re

from django.db.models import Q
from edc_dashboard.view_mixins import EdcViewMixin
from edc_constants.constants import ABNORMAL
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import EnrolmentModelWrapper
from .filters import ListboardViewFilters


class ListboardView(
    EdcViewMixin,
    NavbarViewMixin,
    ListboardFilterViewMixin,
    SearchFormViewMixin,
    ListboardView,
):

    listboard_template = "enrolment_listboard_template"
    listboard_url = "enrolment_listboard_url"
    listboard_panel_style = "info"
    listboard_fa_icon = "fa-user-plus"
    listboard_view_filters = ListboardViewFilters()
    listboard_model = "mapitio_subject.enrolment"
    listboard_view_permission_codename = "edc_dashboard.view_enrolment_listboard"

    alternate_search_attr = "hospital_identifier"

    model_wrapper_cls = EnrolmentModelWrapper
    navbar_selected_item = "enrolled_subject"
    ordering = "-report_datetime"
    paginate_by = 10
    search_form_url = "enrolment_listboard_url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            enrolment_add_url=self.get_enrolment_add_url(), ABNORMAL=ABNORMAL,
        )
        return context

    def get_enrolment_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

    # def get_queryset_filter_options(self, request, *args, **kwargs):
    #     options = super().get_queryset_filter_options(request, *args, **kwargs)
    #     if kwargs.get("subject_identifier"):
    #         options.update({"subject_identifier": kwargs.get("subject_identifier")})
    #     return options

    def extra_search_options(self, search_term):
        q_objects = []
        if re.match("^[A-Z\-]+$", search_term):
            q_objects.append(Q(initials__exact=search_term.upper()))
        q_objects.append(
            Q(subject_identifier__icontains=search_term.replace("-", "").upper())
        )
        if re.match("^[0-9]+$", search_term):
            q_objects.append(Q(hospital_identifier__exact=search_term))
        return q_objects
