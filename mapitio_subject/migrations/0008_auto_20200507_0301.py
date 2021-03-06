# Generated by Django 3.0.4 on 2020-05-07 00:01

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.date_estimated
import edc_model.models.fields.other_charfield
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("mapitio_lists", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mapitio_subject", "0007_auto_20200506_2144"),
    ]

    operations = [
        migrations.CreateModel(
            name="HivFollowup",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "diabetic",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="When the patient first enrolled at the clinic, did they have <u>diabetes</u>?",
                    ),
                ),
                (
                    "diabetes_dx_date_known",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="Is the <u>diabetes</u> diagnosis date known?",
                    ),
                ),
                (
                    "diabetes_dx_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="<u>Diabetes</u> diagnosis date",
                    ),
                ),
                (
                    "diabetes_dx_date_estimated",
                    edc_model.models.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("N/A", "Not applicable"),
                            ("not_estimated", "No."),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        default="N/A",
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is the <u>diabetes</u> diagnosis date estimated?",
                    ),
                ),
                (
                    "other_diabetes_rx",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "hypertensive",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="When the patient enrolled at the clinic, did they have <u>hypertension</u>?",
                    ),
                ),
                (
                    "hypertension_dx_date_known",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="Is the <u>hypertension</u> diagnosis date known?",
                    ),
                ),
                (
                    "hypertension_dx_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="<u>Hypertension</u> diagnosis date",
                    ),
                ),
                (
                    "hypertension_dx_date_estimated",
                    edc_model.models.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("N/A", "Not applicable"),
                            ("not_estimated", "No."),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        default="N/A",
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is the <u>hypertension</u> diagnosis date estimated?",
                    ),
                ),
                (
                    "other_hypertension_rx",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "arv_modification",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Have there been any modifications to the patient's ARV regimen since enrollment?",
                    ),
                ),
                (
                    "arv_modification_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Most <u>recent</u> date ARV regimen changed",
                    ),
                ),
                (
                    "arv_regimen_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "dtg_switched",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the patient ever been switched to a DTG-based regimen?",
                    ),
                ),
                (
                    "dtg_switched_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Date patient initiated on or switched to a DTG-base regimen",
                    ),
                ),
                (
                    "arv_regimen",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="mapitio_lists.ArvRegimens",
                        verbose_name="Most recent ARV Regimen",
                    ),
                ),
                (
                    "diabetes_rx",
                    models.ManyToManyField(
                        blank=True,
                        to="mapitio_lists.DiabetesMedications",
                        verbose_name="Diabetes treatment",
                    ),
                ),
                (
                    "hypertension_rx",
                    models.ManyToManyField(
                        blank=True,
                        to="mapitio_lists.HypertensionMedications",
                        verbose_name="Hypertension treatment",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="mapitio_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "HIV Followup",
                "verbose_name_plural": "HIV Followup",
                "abstract": False,
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalHivFollowup",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "diabetic",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="When the patient first enrolled at the clinic, did they have <u>diabetes</u>?",
                    ),
                ),
                (
                    "diabetes_dx_date_known",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="Is the <u>diabetes</u> diagnosis date known?",
                    ),
                ),
                (
                    "diabetes_dx_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="<u>Diabetes</u> diagnosis date",
                    ),
                ),
                (
                    "diabetes_dx_date_estimated",
                    edc_model.models.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("N/A", "Not applicable"),
                            ("not_estimated", "No."),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        default="N/A",
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is the <u>diabetes</u> diagnosis date estimated?",
                    ),
                ),
                (
                    "other_diabetes_rx",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "hypertensive",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="When the patient enrolled at the clinic, did they have <u>hypertension</u>?",
                    ),
                ),
                (
                    "hypertension_dx_date_known",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="Is the <u>hypertension</u> diagnosis date known?",
                    ),
                ),
                (
                    "hypertension_dx_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="<u>Hypertension</u> diagnosis date",
                    ),
                ),
                (
                    "hypertension_dx_date_estimated",
                    edc_model.models.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("N/A", "Not applicable"),
                            ("not_estimated", "No."),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        default="N/A",
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is the <u>hypertension</u> diagnosis date estimated?",
                    ),
                ),
                (
                    "other_hypertension_rx",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "arv_modification",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Have there been any modifications to the patient's ARV regimen since enrollment?",
                    ),
                ),
                (
                    "arv_modification_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Most <u>recent</u> date ARV regimen changed",
                    ),
                ),
                (
                    "arv_regimen_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "dtg_switched",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the patient ever been switched to a DTG-based regimen?",
                    ),
                ),
                (
                    "dtg_switched_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Date patient initiated on or switched to a DTG-base regimen",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "arv_regimen",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="mapitio_lists.ArvRegimens",
                        verbose_name="Most recent ARV Regimen",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="mapitio_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical HIV Followup",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name="hivfollowup",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="mapitio_sub_subject_5f06a1_idx",
            ),
        ),
    ]
