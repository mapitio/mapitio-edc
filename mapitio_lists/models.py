from edc_list_data.model_mixins import ListModelMixin


class ArvRegimens(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "ARV Regimens"
        verbose_name_plural = "ARV Regimens"


class Conditions(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Conditions"
        verbose_name_plural = "Conditions"


class DiabetesTreatment(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Diabetes Treatment"
        verbose_name_plural = "Diabetes Treatment"


class OffstudyReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Offstudy Reasons"
        verbose_name_plural = "Offstudy Reasons"


class HypertensionTreatment(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Hypertension Treatment"
        verbose_name_plural = "Hypertension Treatment"


class VisitReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Visit Reasons"
        verbose_name_plural = "Visit Reasons"
