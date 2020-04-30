from edc_subject_dashboard.views import SubjectDashboardView


class DashboardView(SubjectDashboardView):

    consent_model = "mapitio_consent.subjectconsent"
    navbar_selected_item = "consented_subject"
    visit_model = "mapitio_subject.subjectvisit"
