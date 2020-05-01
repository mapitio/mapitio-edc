from edc_subject_dashboard.views import SubjectDashboardView
from mapitio_screening.models import SubjectScreening


class DashboardView(SubjectDashboardView):

    consent_model = "mapitio_consent.subjectconsent"
    navbar_selected_item = "consented_subject"
    visit_model = "mapitio_subject.subjectvisit"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(subject_screening=self.subject_screening)
        return context

    @property
    def subject_screening(self):
        return SubjectScreening.objects.get(subject_identifier=self.subject_identifier)
