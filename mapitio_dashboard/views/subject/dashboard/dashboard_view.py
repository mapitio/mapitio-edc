from edc_subject_dashboard.views import SubjectDashboardView


class DashboardView(SubjectDashboardView):

    consent_model = "inte_consent.subjectconsent"
    navbar_selected_item = "consented_subject"
    visit_model = "inte_subject.subjectvisit"
