# Generated by Django 3.0.4 on 2020-05-12 00:09

from django.db import migrations
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):

    dependencies = [
        ("mapitio_consent", "0003_auto_20200504_0014"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="ctc_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                verbose_name="CTC Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="file_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text="Patient file number from Hindu Mandal Hospital (Encryption: RSA local)",
                max_length=71,
                verbose_name="Patient File number",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text="Hindu Mandal Hospital Identifier (Encryption: RSA local)",
                max_length=71,
                verbose_name="HMS Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="ctc_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                null=True,
                unique=True,
                verbose_name="CTC Identifier",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="file_number",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Patient file number from Hindu Mandal Hospital (Encryption: RSA local)",
                max_length=71,
                unique=True,
                verbose_name="Patient File number",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="hospital_identifier",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text="Hindu Mandal Hospital Identifier (Encryption: RSA local)",
                max_length=71,
                unique=True,
                verbose_name="HMS Identifier",
            ),
        ),
    ]
