"""hosproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hosapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),

    path('login/', views.Admin_login_view, name='login'),
    path('register/', views.Admin_register, name='register'),

    path('login1/', views.Doctor_login_view, name='login1'),
    path('register1/', views.Doctor_register, name='register1'),


    path('login2/', views.Patients_login_view, name='login2'),
    path('register2/', views.Patient_register, name='register2'),


    path('patiententer/', views.patiententer, name='patiententer'),
    path('Adminenter/', views.Adminenter, name='Adminenter'),
    path('doctorenter/', views.doctorenter, name='doctorenter'),


    path('data1/', views.ADocreg, name='doct1'),
    path('data2/', views.Apatreg, name='pat1'),
    path('data300/', views.apdnm, name='adoctorname'),
    path('data3/', views.Astaffreg, name='staff1'),
    path('Rec1/', views.Adocrec, name='adocrec1'),
    path('Rec12/', views.Adocrec3, name='adocrec12'),
    path('Rec2/', views.Apatrec, name='patrec1'),
    path('REc3/', views.Astaffrec, name='staffrec1'),


    path('discharge/<str:username>', views.Discharge, name='discharge'),
    path('admin_discharge/', views.Adminenter_discharge, name='admindischarge'),

    path('download_bill/<str:username>', views.Download, name='download'),



    path('ApproveappointData/', views.Approve_appointment_rec, name='Approve_appoint'),
    path('AdminApproveappointData/', views.Admin_Approve_appointment_rec, name='Admin_Approve_appoint'),
    path('admin_book_appointment_pat/<str:username>', views.Admin_book_appointment_pat, name='Admin_book_appointment_pat'),
    path('Admin_Approve_patient/', views.Approve_patients_appoint, name='Admin_Approve_patient_appointment'),
    path('Adminenter_appointent/', views.Adminenter_appointment, name='Adminennter_appointment'),




    path('Doctorenter_Appointmentpatient/', views.doctorenter_appointment_view, name='Doctorennter_patient_appointment_view'),
    path('Doctorenter_recordpatient/', views.doctorenter_appointment_record, name='Doctorennter_patient_appointment_rec'),
    path('Doctorenter_dischargepatient/', views.doctorenter_discharge_record, name='Doctorennter_patient_discharge_rec'),
    path('Doctorenter_deleteappointent/', views.doctorenter_appointment_delete, name='Doctorennter_appointment_delete'),
    path('Doctorenter_reportview/', views.doctorenter_report_view, name='doctorenter_report_view'),



    path('Approve1/', views.AdocApprove, name='Approve'),
    path('Approve2/', views.ApatApprove, name='Approve1'),

    path('edit1/<int:id>/', views.Adocedit, name='edit1'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>', views.destroy, name='delete1'),
    path('edit2/<int:id>/', views.Apatedit, name='edit2'),
    path('update2/<int:id>/', views.update_view1, name='update1'),
    path('delete1/<int:id>', views.destroy1, name='delete2'),
    path('delete2/<str:username>', views.destroy2, name='delete3'),
    path('Appoint/<str:username>/', views.Appoint_view, name='Appoint'),
    path('report/<str:username>/', views.Report, name= 'report'),
    path('patrectoreport/', views.patrectoreport, name= 'patrectoreport'),
    path('generatereport/<str:username>', views.Formreport, name='generatedreport'),
    path('patrectoreportview/', views.patrectoreportview, name= 'patrectoreportview'),


    path('patient_download_bill/<str:username>', views.patient_download_their,name='patient_download_their'),





]
