# Generated by Django 3.0.4 on 2020-04-30 21:52

from django.db import migrations, models
import edc_model.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ("mapitio_subject", "0006_auto_20200430_2049"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="albumin_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Albumin date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="alp_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALP date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="alt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="amylase_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Amylase date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="ast_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>AST date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="cd4_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>CD4 date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="ggt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>GGT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="hbsag_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HbSAg date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="hcv_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HCV date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="hdl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="ldl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>LDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="serum_creatinine_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum creatinine date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="serum_urea_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum urea date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="serum_uric_acid_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum uric acid date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="total_cholesterol_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Total cholesterol date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="triglycerides_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Triglycerides date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalfollowup",
            name="vl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Viral load date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="albumin_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Albumin date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="alp_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALP date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="alt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="amylase_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Amylase date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="ast_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>AST date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="cd4_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>CD4 date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="ggt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>GGT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="hbsag_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HbSAg date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="hcv_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HCV date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="hdl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="ldl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>LDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="serum_creatinine_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum creatinine date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="serum_urea_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum urea date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="serum_uric_acid_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum uric acid date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="total_cholesterol_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Total cholesterol date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="triglycerides_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Triglycerides date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="biomedicalhistory",
            name="vl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Viral load date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="cardiomyopathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Ischaemic cardiomyopathy",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="chronic_renal_failure",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Chronic renal failure",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                max_length=25,
                verbose_name="Were there any other complications to report?",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="diabetic_foot",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Diabetic foot",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="diabetic_retinopathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Diabetic retinopathy",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="peripheral_neuropathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Peripheral neuropathy",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="peripheral_vascular",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Peripheral vascular disease",
            ),
        ),
        migrations.AlterField(
            model_name="complications",
            name="stroke",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Stroke",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="albumin_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Albumin date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="alp_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALP date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="alt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="amylase_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Amylase date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="ast_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>AST date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="cd4_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>CD4 date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="ggt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>GGT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="hbsag_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HbSAg date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="hcv_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HCV date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="hdl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="ldl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>LDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="serum_creatinine_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum creatinine date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="serum_urea_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum urea date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="serum_uric_acid_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum uric acid date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="total_cholesterol_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Total cholesterol date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="triglycerides_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Triglycerides date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalfollowup",
            name="vl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Viral load date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="albumin_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Albumin date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="alp_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALP date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="alt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>ALT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="amylase_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum Amylase date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="ast_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>AST date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="cd4_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>CD4 date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="ggt_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>GGT date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="hbsag_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HbSAg date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="hcv_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HCV date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="hdl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>HDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="ldl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>LDL date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="serum_creatinine_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum creatinine date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="serum_urea_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum urea date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="serum_uric_acid_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Serum uric acid date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="total_cholesterol_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Total cholesterol date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="triglycerides_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Triglycerides date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbiomedicalhistory",
            name="vl_date",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[
                    edc_model.validators.date.date_is_past,
                    edc_model.validators.date.date_is_not_now,
                ],
                verbose_name="<i>Viral load date</i>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="cardiomyopathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Ischaemic cardiomyopathy",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="chronic_renal_failure",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Chronic renal failure",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                max_length=25,
                verbose_name="Were there any other complications to report?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="diabetic_foot",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Diabetic foot",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="diabetic_retinopathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Diabetic retinopathy",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="peripheral_neuropathy",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Peripheral neuropathy",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="peripheral_vascular",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Peripheral vascular disease",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomplications",
            name="stroke",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                null=True,
                verbose_name="Stroke",
            ),
        ),
    ]