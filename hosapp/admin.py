from django.contrib import admin
from hosapp.models import User

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['id', 'username','pFname', 'pLname', 'dFname', 'dLname','phone', 'age', 'gender','password',
                  'address','category', 'department','dob','Admit_date','Approve','Problem_pat','stf_Fname','stf_Lname',
                  'Discharge','roomcharge','doctorcharge','medicinecharge','othercharge','totalcharge','cardiovascular',
                  'Pulmonary','Gastroenterology','Neurology','Musculoskeleton','Gentiourinary','Oro','Extremities','Hernia',
                  'Hydrocele','Varicose','Eyeright','Eyeleft','Earright','Earleft','other','chestxray','impression','rbc','plus',
                  'epithelial','pregnancy','wbc','Neutrophils','Lymphocytes','Eosinophils','monocytes','basophils','hemoglobin',
                  'malaria','filaria','sugar','urea','creatine','bilirubin','sgpt','scot','hiv','hbsag','vdrl','tpha','bloodgroup'] 
admin.site.register(User,userAdmin) 