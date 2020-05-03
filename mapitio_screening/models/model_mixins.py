from django.db import models
from django.utils.safestring import mark_safe
from uuid import uuid4


class MapitioAdditionalIdentifiersModelMixin(models.Model):

    hospital_identifier = models.CharField(
        verbose_name="HMS Identifier",
        max_length=36,
        help_text="Hindu Mandal Hospital Identifier",
        unique=True,
        default=uuid4,
    )

    ctc_identifier = models.CharField(
        verbose_name="CTC Identifier",
        max_length=36,
        null=True,
        blank=True,
        unique=True,
        default=uuid4,
    )

    file_number = models.CharField(
        verbose_name="Patient File number",
        max_length=36,
        help_text=mark_safe("Patient file number from Hindu Mandal Hospital"),
        unique=True,
        default=uuid4,
    )

    class Meta:
        abstract = True
