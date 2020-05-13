# Generated by Django 3.0.6 on 2020-05-12 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mapitio_lists", "0002_auto_20200513_0023"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="arvregimens",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "ARV Regimens",
                "verbose_name_plural": "ARV Regimens",
            },
        ),
        migrations.AlterModelOptions(
            name="chestxrayfindings",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Chest X-ray Findings",
                "verbose_name_plural": "Chest X-ray Findings",
            },
        ),
        migrations.AlterModelOptions(
            name="cholesterolmedications",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Cholesterol Medications",
                "verbose_name_plural": "Cholesterol Medications",
            },
        ),
        migrations.AlterModelOptions(
            name="conditions",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Conditions",
                "verbose_name_plural": "Conditions",
            },
        ),
        migrations.AlterModelOptions(
            name="diabetesmedications",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Diabetes Medications",
                "verbose_name_plural": "Diabetes Medications",
            },
        ),
        migrations.AlterModelOptions(
            name="diagnoses",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Diagnoses",
                "verbose_name_plural": "Diagnoses",
            },
        ),
        migrations.AlterModelOptions(
            name="ecgfindings",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "ECG Findings",
                "verbose_name_plural": "ECG Findings",
            },
        ),
        migrations.AlterModelOptions(
            name="echofindings",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "ECHO Findings",
                "verbose_name_plural": "ECHO Findings",
            },
        ),
        migrations.AlterModelOptions(
            name="hypertensionmedications",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Hypertension Medications",
                "verbose_name_plural": "Hypertension Medications",
            },
        ),
        migrations.AlterModelOptions(
            name="offstudyreasons",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Offstudy Reasons",
                "verbose_name_plural": "Offstudy Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="visitreasons",
            options={
                "ordering": ["display_index", "display_name"],
                "verbose_name": "Visit Reasons",
                "verbose_name_plural": "Visit Reasons",
            },
        ),
    ]