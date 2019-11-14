from django.db import models

# Create your models here.
sex = (
    (1, 'MALE'),
    (2, 'FEMALE')
)

arv = (
    (1, 'AZT + 3TC + NVP'),
    (2, 'AZT + 3TC + EFV'),
    (3, 'AZT + 3TC + DTG'),
    (4, 'ABC + 3TC + EFV'),
    (5, 'ABC + 3TC + DTG'),
    (6, 'd4T + 3TC + NVP'),
    (7, 'd4T + 3TC + EFV'),
    (8, 'TDF + FTC + EFV'),
    (9, 'TDF + FTC + NVP'),
    (10, 'TDF + 3TC + EFV'),
    (11, 'TDF + 3TC + NVP'),
    (12, 'TDF + 3TC + DTG'),
    (13, 'TDF + FTC + DTG'),
    (14, 'TDF + 3TC + ATV/r'),
    (15, 'TDF + FTC + ATV/r'),
    (16, 'TDF + 3TC + LPV/r'),
    (17, 'AZT + 3TC + ATV/r'),
    (18, 'AZT + 3TC + LPV/r'),
    (19, 'ABC + 3TC + ATV/r'),
    (20, 'ABC + 3TC + LPV/r'),
    (21, 'TDF + FTC + LPV/R'),
    (22, 'DTG + (ABC/3TC) + ATV/r'),
)

diabetes = (
    (1, 'Yes'),
    (2, 'No')
)

hypertension = (
    (1, 'Yes'),
    (2, 'No')
)

blood_sugar = (
    (1, 'Fasting'),
    (2, 'Random')

)

x_ray = (
    (1, 'Normal'),
    (2, 'Pneumonia'),
    (3, 'PCP'),
    (4, 'Cardiomegaly'),
    (5, 'Pleural effusion')
)

ecg = (
    (1, 'Normal'),
    (2, 'Left ventricular hypertrophy'),
    (3, 'Ischaemic heart disease'),
    (4, 'Heart arrhythmias'),
)

echo = (
    (1, 'Normal'),
    (2, 'Left ventricular hypertrophy'),
    (3, 'Dystolic dysfunction'),
    (4, 'Cardiomyopathy'),
    (5, 'Other')
)

incare = (
    (1, 'Yes, alive and in care at this clinic'),
    (2, 'Yes, alive and in care elsewhere'),
    (3, 'No, patient died'),
)

choices = (
    (1, 'Yes'),
    (2, 'No')
)


class EnrolmentPatientStartAtTheClinic(models.Model):
    Date_of_form_completion = models.DateField()
    Patient_Hospital_ID = models.CharField(max_length=20)
    Date_of_Birth = models.DateField()
    Age = models.IntegerField()
    Sex = models.IntegerField(choices=sex)
    Date_patient_enrolled_at_the_clinic = models.DateField()
    When_was_the_diagnosis_made = models.DateField()
    Date_antiretroviral_therapy_commenced = models.DateField()
    Current_ARV_regimen = models.IntegerField(choices=arv)
    Previous_regimen_1_Date_commenced = models.DateField()
    Previous_regimen_1_Date_ended = models.DateField()
    Previous_regimen_1_Reason_for_shift = models.TextField()
    Previous_regimen_2_Date_commenced = models.DateField()
    Previous_regimen_2_Date_ended = models.DateField()
    Previous_regimen_2_Reason_for_shift = models.TextField()
    Did_the_patient_have_Diabetes_when_they_started_attending_the_clinic = models.IntegerField(choices=diabetes)
    If_YES_when_was_the_diagnosis_of_diabetes_made = models.DateField()
    List_of_diabetes_treatment_when_patient_started_attending_the_clinic = models.TextField()
    Did_the_patient_have_Hypertension_when_they_started_attending_the_clinic = models.IntegerField(choices=diabetes)
    If_YES_when_was_the_diagnosis_of_hypertension_made = models.DateField()
    List_of_hypertension_treatment_when_patient_started_attending_the_clinic = models.TextField()
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Waist = models.IntegerField()
    Blood_pressure_systolic = models.IntegerField()
    Blood_pressure_diastolic = models.IntegerField()
    Blood_glucose = models.DecimalField(decimal_places=1, max_digits=3)
    Was_this_a_fasting_or_random_blood_glucose = models.IntegerField(choices=blood_sugar)
    Total_cholesterol = models.DecimalField(decimal_places=1, max_digits=3)
    LDL = models.DecimalField(decimal_places=1, max_digits=3)
    HDL = models.DecimalField(decimal_places=1, max_digits=3)
    Triglycerides = models.DecimalField(decimal_places=1, max_digits=3)
    Serum_urea_levels = models.DecimalField(decimal_places=1, max_digits=3)
    Serum_creatinine_levels = models.DecimalField(decimal_places=1, max_digits=3)
    CD4_count = models.IntegerField()
    Date_of_CD4_count = models.DateField()
    Viral_load = models.IntegerField()
    Date_of_Viral_load = models.DateField()
    Chest_X_ray_option_1 = models.IntegerField(choices=x_ray)
    Chest_X_ray_option_2 = models.IntegerField(choices=x_ray, default=None)
    ECG_findings = models.IntegerField(choices=ecg)
    ECHO_findings = models.IntegerField(choices=echo)


class HIVRetrospectiveCohortFollowUpCRF(models.Model):
    Qn1_Date_of_form_completion = models.DateField()
    Qn2_Patient_Hospital_ID = models.CharField(max_length=20)
    Patients_initials = models.CharField(max_length=3)
    Qn3_Date_patient_last_seen_at_the_clinic = models.DateField()
    Qn4_Is_the_patient_alive_and_in_care = models.IntegerField(choices=incare)
    Qn5_Since_the_patient_started_at_this_clinic_have_they_developed_diabetes = models.IntegerField(choices=diabetes)
    Qn6_If_YES_when_was_the_diagnosis_of_diabetes_made = models.DateField()
    Qn7_List_of_diabetes_treatment = models.TextField()
    Qn8_Since_the_patient_started_at_this_clinic_have_they_developed_hypertension = models.IntegerField(choices=hypertension)
    Qn9_If_YES_when_was_the_diagnosis_of_hypertension_made = models.DateField()
    Qn10_List_of_hypertension_treatment = models.TextField()
    Qn11_Stroke = models.IntegerField(choices=choices)
    If_yes_to_Qn11_question_date_of_diagnosis = models.DateField()
    Qn12_Diabetic_foot = models.IntegerField(choices=choices)
    If_yes_to_Qn12_date_of_diagnosis = models.DateField()
    Qn13_Chronic_heart_failure = models.IntegerField(choices=choices)
    If_yes_to_Qn13_question_date_of_diagnosis = models.DateField()
    Qn14_Chronic_renal_failure = models.IntegerField(choices=choices)
    If_yes_to_Qn14_date_of_diagnosis = models.DateField()
