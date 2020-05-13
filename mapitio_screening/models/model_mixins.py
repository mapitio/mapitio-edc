from django.db import models
from django.utils.safestring import mark_safe
from django_crypto_fields.fields import EncryptedCharField


class MapitioAdditionalIdentifiersModelMixin(models.Model):

    hospital_identifier = EncryptedCharField(
        verbose_name="HMS Identifier",
        help_text="Hindu Mandal Hospital Identifier",
        unique=True,
    )

    ctc_identifier = EncryptedCharField(
        verbose_name="CTC Identifier", null=True, blank=True, unique=True,
    )

    file_number = EncryptedCharField(
        verbose_name="Patient File number",
        help_text=mark_safe("Patient file number from Hindu Mandal Hospital"),
        unique=True,
    )

    class Meta:
        abstract = True
