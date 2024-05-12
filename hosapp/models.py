from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    Approve = models.BooleanField('Approve', default=False)
    Appoint = models.BooleanField('Appoint', default=False)
    Discharge = models.BooleanField('Discharge', default=False)

    username = models.CharField(max_length=70, unique=True)
    pFname = models.CharField(max_length=70, null=True)
    pLname = models.CharField(max_length=70, null=True)
    dFname = models.CharField(max_length=70, null=True)
    dLname = models.CharField(max_length=70, null=True)
    stf_Fname = models.CharField(max_length=70, null=True)
    stf_Lname = models.CharField(max_length=70, null=True)
    Dphone = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    Admit_date = models.DateField(null=True)
    Discharge_date = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=70)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    Ailment = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    Problem_pat = models.CharField(max_length=1000, null=True)
    roomcharge = models.IntegerField(null=True)
    doctorcharge = models.IntegerField(null=True)
    medicinecharge = models.IntegerField(null=True)
    othercharge = models.IntegerField(null=True)
    totalcharge = models.IntegerField(null=True)


    # ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,report field............................................
    
    cardiovascular=models.CharField(max_length=1000,null=True)
    Pulmonary=models.CharField(max_length=1000,null=True)
    Gastroenterology=models.CharField(max_length=1000,null=True)
    Neurology=models.CharField(max_length=1000,null=True)
    Musculoskeleton=models.CharField(max_length=1000,null=True)
    Gentiourinary=models.CharField(max_length=1000,null=True)
    Oro=models.CharField(max_length=1000,null=True)
    Extremities=models.CharField(max_length=1000,null=True)
    Hernia=models.CharField(max_length=1000,null=True)
    Hydrocele=models.CharField(max_length=1000,null=True)
    Varicose=models.CharField(max_length=1000,null=True)
    Eyeright=models.CharField(max_length=1000,null=True)
    Eyeleft=models.CharField(max_length=1000,null=True)
    Earright=models.CharField(max_length=1000,null=True)
    Earleft=models.CharField(max_length=1000,null=True)
    other=models.CharField(max_length=1000,null=True)
    chestxray=models.CharField(max_length=1000,null=True)
    impression=models.CharField(max_length=1000,null=True)
    rbc=models.CharField(max_length=1000,null=True)
    plus=models.CharField(max_length=1000,null=True)
    epithelial=models.CharField(max_length=1000,null=True)
    pregnancy=models.CharField(max_length=1000,null=True)


    wbc=models.CharField(max_length=1000,null=True)
    Neutrophils=models.CharField(max_length=1000,null=True)
    Lymphocytes=models.CharField(max_length=1000,null=True)
    Eosinophils=models.CharField(max_length=1000,null=True)
    monocytes=models.CharField(max_length=1000,null=True)
    basophils=models.CharField(max_length=1000,null=True)
    hemoglobin=models.CharField(max_length=1000,null=True)
    malaria=models.CharField(max_length=1000,null=True)
    filaria=models.CharField(max_length=1000,null=True)
    sugar=models.CharField(max_length=1000,null=True)
    urea=models.CharField(max_length=1000,null=True)
    creatine=models.CharField(max_length=1000,null=True)
    bilirubin=models.CharField(max_length=1000,null=True)
    sgpt=models.CharField(max_length=1000,null=True)
    scot=models.CharField(max_length=1000,null=True)
    hiv=models.CharField(max_length=1000,null=True)
    hbsag=models.CharField(max_length=1000,null=True)
    vdrl=models.CharField(max_length=1000,null=True)
    tpha=models.CharField(max_length=1000,null=True)
    bloodgroup=models.CharField(max_length=1000,null=True)

    def save(self, *args, **kwargs):
        if self.is_doctor and not self.dFname:
            self.dFname = self.username
        elif self.is_patient and not self.pFname:
            self.pFname = self.username

        if not self.Discharge_date:
            self.Discharge_date = timezone.now().date()

        super().save(*args, **kwargs)
