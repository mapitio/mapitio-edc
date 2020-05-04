from django.db import models
from django.utils.safestring import mark_safe


class MapitioAdditionalIdentifiersModelMixin(models.Model):

    hospital_identifier = models.CharField(
        verbose_name="HMS Identifier",
        max_length=36,
        help_text="Hindu Mandal Hospital Identifier",
        unique=True,
    )

    ctc_identifier = models.CharField(
        verbose_name="CTC Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True,
    )

    file_number = models.CharField(
        verbose_name="Patient File number",
        max_length=36,
        help_text=mark_safe("Patient file number from Hindu Mandal Hospital"),
        unique=True,
    )

    class Meta:
        abstract = True
