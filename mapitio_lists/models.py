from edc_list_data.model_mixins import ListModelMixin


class ArvRegimens(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "ARV Regimens"
        verbose_name_plural = "ARV Regimens"


class Conditions(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Conditions"
        verbose_name_plural = "Conditions"


class DiabetesMedications(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Diabetes Medications"
        verbose_name_plural = "Diabetes Medications"


class ChestXrayFindings(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Chest X-ray Findings"
        verbose_name_plural = "Chest X-ray Findings"


class CholesterolMedications(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Cholesterol Medications"
        verbose_name_plural = "Cholesterol Medications"


class Diagnoses(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Diagnoses"
        verbose_name_plural = "Diagnoses"


class EchoFindings(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "ECHO Findings"
        verbose_name_plural = "ECHO Findings"


class EcgFindings(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "ECG Findings"
        verbose_name_plural = "ECG Findings"


class OffstudyReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Offstudy Reasons"
        verbose_name_plural = "Offstudy Reasons"


class HypertensionMedications(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Hypertension Medications"
        verbose_name_plural = "Hypertension Medications"


class VisitReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Visit Reasons"
        verbose_name_plural = "Visit Reasons"
