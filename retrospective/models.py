from django.db import models

from edc_constants.choices import YES_NO, GENDER

from .choices import BLOOD_SUGAR, ARV, X_RAY, ECG, ECHO, IN_CARE


class Enrolment(models.Model):
    date_of_completion = models.DateField(
        verbose_name="Date of form completion", default=None
    )
    hospital_id = models.CharField(
        max_length=20, verbose_name="Patient Hospital ID", default=None
    )
    birthday = models.DateField(verbose_name="Date of birth", default=None)
    age = models.CharField(max_length=3, verbose_name="Age", default=0)
    sex = models.CharField(
        max_length=6, choices=GENDER, verbose_name="Sex", default=None
    )
    enrolled_date = models.DateField(
        verbose_name="Date patient enrolled at the clinic", default=None
    )
    diagnosis_made = models.DateField(
        verbose_name="When was the diagnosis made?", default=None
    )
    date_arv_commenced = models.DateField(
        verbose_name="Date antiretroviral therapy commenced", default=None
    )
    current_arv_regimen = models.CharField(
        max_length=2, choices=ARV, verbose_name="Current ARV regimen", default=None
    )
    regimen1_commenced = models.DateField(verbose_name="Date commenced", default=None)
    regimen1_end = models.DateField(verbose_name="Date ended", default=None)
    regime1_reason_for_shift = models.TextField(
        verbose_name="Reason for switching", default=None
    )
    regimen2_commenced = models.DateField(verbose_name="Date commenced", default=None)
    regimen2_ended = models.DateField(verbose_name="Date ended", default=None)
    regimen2_reason_for_shift = models.TextField(
        verbose_name="Reason for switching", default=None
    )
    diabetes_status = models.IntegerField(
        choices=YES_NO,
        verbose_name="Did the patient have Diabetes when they "
        "started attending the clinic?",
        default=None,
    )
    diagnosis_diabetes = models.DateField(
        verbose_name="If YES, when was the diagnosis of diabetes made?", default=None
    )
    treatment_diabetes = models.TextField(
        verbose_name="List of diabetes treatment when patient started attending the "
        "clinic",
        default=None,
    )
    hypertension_status = models.IntegerField(
        choices=YES_NO,
        verbose_name="Did the patient have Hypertension when "
        "they started attending the clinic?",
        default=None,
    )
    diagnosis_hypertension = models.DateField(
        verbose_name="If YES, when was the diagnosis of hypertension made?",
        default=None,
    )
    hypertension_treatment = models.TextField(
        verbose_name="List of hypertension treatment when patient started "
        "attending the clinic",
        default=None,
    )
    height = models.IntegerField(verbose_name="Height", default=None)
    weight = models.IntegerField(verbose_name="Weight", default=None)
    waist = models.IntegerField(verbose_name="Waist", default=None)
    bp_systolic = models.IntegerField(
        verbose_name="Blood pressure Systolic (mmHg)", default=None
    )
    bp_diastolic = models.IntegerField(
        verbose_name="Blood pressure Diastolic (mmHg)", default=None
    )
    blood_glucose = models.DecimalField(
        decimal_places=1, max_digits=3, verbose_name="Blood glucose", default=None
    )
    fasting_or_random = models.CharField(
        max_length=4,
        choices=BLOOD_SUGAR,
        verbose_name="Was this a fasting or random blood glucose?",
        default=None,
    )
    total_cholesterol = models.DecimalField(
        decimal_places=1, max_digits=3, verbose_name="Total cholesterol", default=None
    )
    ldl = models.DecimalField(
        decimal_places=1, max_digits=3, verbose_name="LDL", default=None
    )
    hdl = models.DecimalField(
        decimal_places=1, max_digits=3, verbose_name="HDL", default=None
    )
    triglycerides = models.DecimalField(
        decimal_places=1, max_digits=3, verbose_name="Triglycerides", default=None
    )
    serum_urea_levels = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        verbose_name="Serum urea levels (mg/dl)",
        default=None,
    )
    Serum_creatinine_levels = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        verbose_name="Serum creatinine levels (mg/dl)",
        default=None,
    )
    cd4_count = models.IntegerField(verbose_name="CD4 count", default=None)
    date_of_CD4_count = models.DateField(verbose_name="Date of CD4 count", default=None)
    viral_load = models.IntegerField(verbose_name="Viral load", default=None)
    date_of_Viral_load = models.DateField(
        verbose_name="Date of Viral load", default=None
    )
    chest_X_ray_option_1 = models.IntegerField(
        choices=X_RAY,
        verbose_name="Chest X-ray Choose from findings listed (" "you can enter up to",
        default=None,
    )
    ecg_findings = models.IntegerField(
        choices=ECG, verbose_name="ECG findings", default=None
    )
    echo_findings = models.IntegerField(
        choices=ECHO, verbose_name="ECHO findings", default=None
    )


class FollowUp(models.Model):
    date_completion = models.DateField(
        verbose_name="Date of form completion", default=None
    )
    hospital_id = models.CharField(
        max_length=20, verbose_name="Patient Hospital ID", default=None
    )
    initials = models.CharField(
        max_length=3, verbose_name="Patients initials", default=None
    )
    date_last_seen = models.DateField(
        verbose_name="Date patient last seen at the clinic", default=None
    )
    patient_alive = models.IntegerField(
        choices=IN_CARE, verbose_name="Is the patient alive and in care?", default=None
    )
    developed_diabetes = models.IntegerField(
        choices=YES_NO,
        verbose_name="Since the patient started at this clinic, have they developed diabetes?",
        default=None,
    )
    diagnosis_diabetes_made = models.DateField(
        verbose_name="If YES, when was the diagnosis of diabetes made?", default=None
    )
    diabetes_treatment = models.TextField(
        verbose_name="List of diabetes treatment.", default=None
    )
    developed_hypertension = models.IntegerField(
        choices=YES_NO,
        verbose_name="Since the patient started at this clinic, have they developed hypertension?",
        default=None,
    )
    diagnosis_hypertension_made = models.DateField(
        verbose_name="If YES, when was the diagnosis of hypertension made?",
        default=None,
    )
    hypertension_treatment = models.TextField(
        verbose_name="List of hypertension treatment.", default=None
    )
    stroke = models.IntegerField(choices=YES_NO, verbose_name="Stroke", default=None)
    stroke_diagnosis = models.DateField(
        verbose_name="If yes, date of diagnosis", default=None
    )
    diabetic_foot = models.IntegerField(
        choices=YES_NO, verbose_name="Diabetic foot", default=None
    )
    diabetic_foot_diagnosis = models.DateField(
        verbose_name="If yes, date of diagnosis", default=None
    )
    heart_failure = models.IntegerField(
        choices=YES_NO, verbose_name="Chronic heart failure", default=None
    )
    heart_failure_diagnosis = models.DateField(
        verbose_name="If yes, date of diagnosis", default=None
    )
    renal_failure = models.IntegerField(
        choices=YES_NO, verbose_name="Chronic renal failure", default=None
    )
    renal_failure_diagnosis = models.DateField(
        verbose_name="If yes, date of diagnosis", default=None
    )
