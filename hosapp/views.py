from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from hosapp.forms import SignUpForm,LoginForm,AddDoctorForm,AddPatientForm,Doctor_SignUpForm,Doctor_LoginForm,Patient_SignUpForm,Patients_LoginForm
from hosapp.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    return render(request, 'hosapp/index.html')


# ..............................................................................................................
# ///////////////////////////////////////LOgin and Register of Patients,Doctor and Admin>>>>>>>>>>>>>>>>>>>>>>>

# ????????????????????????????????Admin>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Admin_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/login/')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'hosapp/Admin_sign.html', {'form': form, 'msg': msg})


def Admin_login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('Adminenter')
            elif user is not None and user.is_doctor and user.Approve:
                login(request, user)
                return redirect('doctorenter')
            elif user is not None and user.is_patient and user.Approve:
                login(request, user)
                return redirect('patiententer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'hosapp/Admin_login.html', {'form': form, 'msg': msg})

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Docotor<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Doctor_register(request):
    msg = None
    if request.method == 'POST':
        form = Doctor_SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/login1/')
        else:
            msg = 'form is not valid'
    else:
        form = Doctor_SignUpForm()
    return render(request,'hosapp/Doctor_sign.html', {'form': form, 'msg': msg})




def Doctor_login_view(request):
    form = Doctor_LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin and user.Approve:
                login(request, user)
                return redirect('login1')
            elif user is not None and user.is_doctor and user.Approve:
                login(request, user)
                return redirect('doctorenter')
            elif user is not None and user.is_patient and user.Approve:
                login(request, user)
                return redirect('loin1')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'hosapp/Doctor_login.html', {'form': form, 'msg': msg})

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Patients>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>?


def Patient_register(request):
    msg = None
    if request.method == 'POST':
        form = Patient_SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/login2/')
        else:
            msg = 'form is not valid'
    else:
        form = Patient_SignUpForm()
    return render(request,'hosapp/patient_sign.html', {'form': form, 'msg': msg})

def Patients_login_view(request):
    form = Patients_LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('login2')
            elif user is not None and user.is_doctor and user.Approve:
                login(request, user)
                return redirect('login2')
            elif user is not None and user.is_patient and user.Approve:
                login(request, user)
                return redirect('patiententer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'hosapp/patients_login.html', {'form': form, 'msg': msg})





# ..........................................................................................................................................

def doctorenter(request):
    userdata201= User.objects.filter(is_patient=True,Approve=True,Appoint=False,dFname=request.user.username).count()
    userdata202= User.objects.filter(is_patient=True,Approve=True,Appoint=True,dFname=request.user.username).count()
    userdata203= User.objects.filter(is_patient=True,Approve=True,Appoint=True,dFname=request.user.username,Discharge=True).count()

    userdata204= User.objects.filter(is_patient=True, Approve=True,dFname=request.user.username).order_by('-id')[:5]



    return render(request,'hosapp/doctor.html',{'userdata204':userdata204,'count201':userdata201,'count202':userdata202,'count203':userdata203})


def patiententer(request):
    return render(request,'hosapp/patient.html')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def Adminenter(request):
    userdata1= User.objects.filter(is_doctor=True, Approve=True).order_by('-id')[:5]
    userdata2= User.objects.filter(is_patient=True, Approve=True).order_by('-id')[:5]
    userdata3 = User.objects.filter(is_doctor=True,Approve=True).count()
    userdata4 = User.objects.filter(is_patient=True,Approve=True).count()
    userdata100 = User.objects.filter(is_doctor=True,Approve=False).count()
    userdata101= User.objects.filter(is_patient=True,Approve=False).count()
    userdata102= User.objects.filter(is_patient=True,Approve=True,Appoint=True).count()
    userdata103= User.objects.filter(is_patient=True,Approve=True,Appoint=False).count()

    return render(request,'hosapp/Admin.html',{'userdata':userdata1,'userdata1':userdata2,'count':userdata3,'count1':userdata4,'count2':userdata100,'count3':userdata101,'count4':userdata102,'count5':userdata103})

    #........................................................................................................//////////////////////////////////////


def ADocreg(request):
    msg = None
    if request.method == 'POST':
        form= AddDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/Approve/')
        else:
            msg = 'form is not valid'
    else:
        form = AddDoctorForm()
    return render(request,'hosapp/Adocrec.html', {'form': form, 'msg': msg})


def Apatreg(request):
    msg = None
    if request.method == 'POST':
        form =AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('/Approve1/')
        else:
            msg = 'form is not valid'
    else:
        form = AddPatientForm()
    return render(request,'hosapp/patientreg.html', {'form': form, 'msg': msg})

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def apdnm(request):
    usernames = User.objects.values_list('dFname', flat=True)
    return render(request,'hosapp/patientreg.html',{'userdata300': usernames})

def Astaffreg(request):
    return render(request,'hosapp/staffreg.html')

# ...................................................................................................////////////////////

def Adocrec(request):
    userdata5= User.objects.filter(is_doctor=True)& User.objects.filter(Approve=True)
    return render(request,'hosapp/Adocrec1.html',{'userdata2':userdata5})

def Adocrec3(request):
    userdata5= User.objects.filter(is_doctor=True)& User.objects.filter(Approve=True)
    return render(request,'hosapp/patPgDoc.html',{'userdata2':userdata5})

def Apatrec(request):
    userdata6 = User.objects.filter(is_patient=True) & User.objects.filter(Approve=True)
    return render(request,'hosapp/patientrec1.html',{'userdata6':userdata6})

def Astaffrec(request):
    return render(request,'hosapp/staffrec1.html')

# ....................................................................................................................

def AdocApprove(request):
    userdata7 = User.objects.filter(is_doctor=True) & User.objects.filter(Approve=False)
    if request.method == 'POST':
        id_list=request.POST.getlist('boxes')
        for x in id_list:
            User.objects.filter(id=int(x)).update(Approve=True)
            return redirect('adocrec1')

        id_list1=request.POST.getlist('boxes1')
        for y in id_list1:
            User.objects.filter(id=int(y)).delete()
            return redirect('Approve')
    return render(request,'hosapp/AdocApprove.html',{'userdata7':userdata7})

def ApatApprove(request):
    userdata8 = User.objects.filter(is_patient=True) & User.objects.filter(Approve=False)
    if request.method == 'POST':
        id_list2=request.POST.getlist('boxes2')
        for z in id_list2:
            User.objects.filter(id=int(z)).update(Approve=True)
            return redirect('patrec1')

        id_list3=request.POST.getlist('boxes3')
        for w in id_list3:
            User.objects.filter(id=int(w)).delete()
            return redirect('Approve1')
    return render(request,'hosapp/Apatapprove.html',{'userdata8':userdata8})


# ........................................................................................./////////////////////////////////////


def Adocedit(request,id):
    data3=User.objects.get(id=id)
    return render(request,'hosapp/Docedit1.html',{'dataa':data3})
def Apatedit(request,id):
    data5=User.objects.get(id=id)
    return render(request,'hosapp/Apatedit.html',{'datap':data5})

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

def update_view(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.dFname = request.POST['dFname']
        user.dLname = request.POST['dLname']
        user.email = request.POST['email']
        user.address = request.POST['add']
        user.Dphone = request.POST['Dphone']
        user.age = request.POST['age']
        user.department = request.POST['department']
        user.save()
        return redirect('adocrec1')
    else:
        user = User.objects.get(id=id)
        context = {'dataa': user}
        return render(request, 'hosapp/Docedit1.html', context)

def update_view1(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.pFname = request.POST['pFname']
        user.pLname = request.POST['pLname']
        user.email = request.POST['email']
        user.address = request.POST['add']
        user.phone = request.POST['phone']
        user.age = request.POST['age']
        user.Ailment = request.POST['Ailment']
        user.save()
        return redirect('patrec1')
    else:
        user = User.objects.get(id=id)
        context = {'datap': user}
        return render(request, 'hosapp/Apatedit.html', context)
    
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
def destroy(request, id):  
    data4 = User.objects.get(id=id)  
    data4.delete()  
    return redirect('adocrec1')
def destroy1(request, id):  
    data4 = User.objects.get(id=id)  
    data4.delete()  
    return redirect('patrec1')

# ................................................................................................................



def Approve_patients_appoint(request):
    userdata_Pat_Appoint = User.objects.filter(is_patient=True, Appoint=False)
    if request.method == 'POST':
        id_list3 = request.POST.getlist('boxes4')
        for pat in id_list3:
                user_instance = get_object_or_404(User, id=int(pat))
                user_instance.Appoint = True
                user_instance.save()

        id_list4 = request.POST.getlist('boxes5')
    
        for apat in id_list4:
            User.objects.filter(id=int(apat)).delete()
            return redirect('Admin_Approve_patient_appointments')


     
    return render(request, 'hosapp/Approve_patients_appoint.html', {'userdata_pat_Appoint': userdata_Pat_Appoint})

# .........................................................................................................................

def Appoint_view(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user.username = request.POST['username']
        user.Admit_date = request.POST['Admit_date']
        user.dFname = request.POST.get('dFname')
        user.department = request.POST['department']
        user.Problem_pat = request.POST['Problem_pat']
        user.Dphone = request.POST['Dphone']
        user.save()
        return redirect('../')
    else:
        user = User.objects.get(username=username)
        context = {'Patient_Appoint': user}
    return render(request, 'hosapp/Appoint_patients.html', context)

# ...................................................................................................................................

def Admin_Approve_appointment_rec(request):
    Adminpatappoit_data= User.objects.filter(is_patient=True,Appoint=True,Approve=True)
    return render(request,'hosapp/appoint_patview_data.html',{'Adminpatappoit_data':Adminpatappoit_data})

def Admin_book_appointment_pat(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)  
        user.username = request.POST['username']
        user.Admit_date = request.POST['Admit_date']
        user.dFname = request.POST.get('dFname')
        user.department = request.POST['department']
        user.Problem_pat = request.POST['Problem_pat']
        user.Dphone = request.POST['Dphone']
        user.address = request.POST['address']
        user.save()  
        return redirect('Admin_Approve_patient_appointment')  

    else:
        
        user = User.objects.get(username=username)  
        context = {'Admin_Appoint': user}  
        return render(request, 'hosapp/admin_book_appointment_pat.html', context) 


    

def Approve_appointment_rec(request):
    Appoint_patients_data= User.objects.filter(is_patient=True,Appoint=True,Approve=True,username=request.user.username)
    return render(request,'hosapp/Approve_Appointment_data.html',{'Appoint_patients_data':Appoint_patients_data})


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def doctorenter_appointment_view(request):
    doctorenter_appointmentdata=User.objects.filter(is_patient=True,Appoint=False,Approve=True,dFname=request.user.username)
    return render(request,'hosapp/Doctorenter_Appointment_viewdata.html',{'doctorenter_appointmentdata':doctorenter_appointmentdata})

def Adminenter_appointment(request):
    Adminenter_appointmentdata=User.objects.filter(is_patient=True,Appoint=False,Approve=True)
    return render(request,'hosapp/Adminenter_Appointment_viewdata.html',{'Adminenter_appointmentdata':Adminenter_appointmentdata})




def doctorenter_appointment_record(request):
    doctorenter_appointmentrecdata = User.objects.filter(is_patient=True, Appoint=True, Approve=True, dFname=request.user.username)
    return render(request, 'hosapp/Doctorenter_Appointment_recorddata.html', {'doctorenter_appointmentrecdata': doctorenter_appointmentrecdata})

def doctorenter_discharge_record(request):
    doctorenter_dischargedata = User.objects.filter(is_patient=True, Appoint=True, Approve=True, Discharge=True, dFname=request.user.username)
    return render(request, 'hosapp/Doctorenter_discharged_data.html', {'doctorenter_dischargedata': doctorenter_dischargedata})

def doctorenter_appointment_delete(request):
    doctorenter_appointmentdelete = User.objects.filter(is_patient=True, Appoint=False, Approve=True, dFname=request.user.username)
    return render(request, 'hosapp/Doctorenter_delete_appointment.html', {'doctorenter_appointmentdelete': doctorenter_appointmentdelete})    

def destroy2(request, username):  
    doctorenter_delete = User.objects.get(username=username)  
    doctorenter_delete.delete()  
    return redirect('Doctorennter_appointment_delete')

def Discharge(request, username):
    try:
        user = User.objects.get(username=username)
        if request.method == 'POST':
            roomcharge = request.POST.get('roomcharge')
            doctorcharge = request.POST.get('doctorcharge')
            medicinecharge = request.POST.get('medicinecharge')
            othercharge = request.POST.get('othercharge')
            totalcharge = request.POST.get('totalcharge')
            
            
            try:
                user.roomcharge = float(roomcharge)
                user.doctorcharge = float(doctorcharge)
                user.medicinecharge = float(medicinecharge)
                user.othercharge = float(othercharge)
                user.totalcharge = float(totalcharge)
            except ValueError:
                
                return render(request, 'error.html', {'error_message': 'Invalid input for charges'})
            
            user.save()
            
            
            number_of_days_spent = (timezone.now().date() - user.Admit_date).days
            context = {'Patientdish': user, 'day': number_of_days_spent, 'timezone': timezone}
            return render(request, 'hosapp/download_bill.html', context)
        
        else:
            number_of_days_spent = (timezone.now().date() - user.Admit_date).days
            context = {'data4': user, 'day': number_of_days_spent, 'timezone': timezone}
            return render(request, 'hosapp/Discharge.html', context)
    except User.DoesNotExist:
        
        return render(request, 'error.html', {'error_message': 'User does not exist'})
def Download(request, username):
    try:
        user = get_object_or_404(User, username=username)
        number_of_days_spent = (timezone.now().date() - user.date_joined.date()).days
        context = {
            'Patientdish': user,
            'day': number_of_days_spent,
            'timezone': timezone,
            'room_charge': user.roomcharge,  
            'doctor_fee': user.doctorcharge,    
            'medicine_cost': user.medicinecharge,  
            'other_charge': user.othercharge,   
            'total_charge': user.totalcharge,    
        }
        return render(request, 'hosapp/download_bill.html', context)
    except User.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'User does not exist'})



def Adminenter_discharge(request):
    Appoint_discharge1= User.objects.filter(is_patient=True,Appoint=True,Approve=True,Discharge=False)
    return render(request, 'hosapp/admin_discharge.html', {'Appoint_discharge1':Appoint_discharge1})


def patrectoreport(request):
    patrectoreport= User.objects.filter(is_patient=True) & User.objects.filter(Approve=True)
    return render(request,'hosapp/patientdatatoreport.html',{'patrectoreport':patrectoreport})

def patrectoreportview(request):
    patrectoreportview= User.objects.filter(is_patient=True) & User.objects.filter(Approve=True)
    return render(request,'hosapp/patientdatatoreportview.html',{'patrectoreportview':patrectoreportview})


def Report(request, username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return render(request, 'error_page.html', {'error_message': 'User does not exist'})

    if request.method == 'POST':
        user.cardiovascular = request.POST['cardiovascular']
        user.Pulmonary = request.POST['Pulmonary']
        user.Gastroenterology = request.POST['Gastroenterology']
        user.Neurology = request.POST['Neurology']
        user.Musculoskeleton = request.POST['Musculoskeleton']
        user.Gentiourinary = request.POST['Gentiourinary']
        user.Oro = request.POST['Oro']
        user.Extremities = request.POST['Extremities']
        user.Hernia = request.POST['Hernia']
        user.Hydrocele = request.POST['Hydrocele']
        user.Varicose = request.POST['Varicose']
        user.Eyeright = request.POST['eyeright']
        user.Eyeleft = request.POST['eyeleft']
        user.Earright = request.POST['earright']
        user.Earleft = request.POST['earleft']
        user.other = request.POST['otherrep']
        user.chestxray = request.POST['chestxray']
        user.impression = request.POST['impression']
        user.rbc = request.POST['rbc']
        user.plus = request.POST['plus']
        user.epithelial = request.POST['epithelial']
        user.pregnancy = request.POST['pregnancy']
        user.wbc = request.POST['wbc']
        user.Neutrophils = request.POST['Neutrophils']
        user.Lymphocytes = request.POST['Lymphocytes']
        user.Eosinophils = request.POST['Eosinophils']
        user.monocytes = request.POST['monocytes']
        user.basophils = request.POST['basophils']
        user.hemoglobin = request.POST['hemoglobin']
        user.malaria = request.POST['malaria']
        user.filaria = request.POST['filaria']
        user.sugar = request.POST['sugar']
        user.urea = request.POST['urea']
        user.creatine = request.POST['creatine']
        user.bilirubin = request.POST['bilirubin']
        user.sgpt = request.POST['sgpt']
        user.scot = request.POST['scot']
        user.hiv = request.POST['hiv']
        user.hbsag = request.POST['hbsag']
        user.vdrl = request.POST['vdrl']
        user.tpha = request.POST['tpha']
        user.bloodgroup = request.POST['bloodgroup']
        user.save()
        return redirect('generatedreport', username=username)



    number_of_days_spent = (timezone.now().date() - user.Admit_date).days
    context = {'report': user, 'day': number_of_days_spent, 'timezone': timezone}
    return render(request, 'hosapp/Report.html', context)

def Formreport(request, username):
    try:
        user = get_object_or_404(User, username=username)
        number_of_days_spent = (timezone.now().date() - user.date_joined.date()).days
        context = {
            'report': user,
            'day': number_of_days_spent,
            'timezone': timezone,   
        }
        return render(request, 'hosapp/generatedreport.html', context)
    except User.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'User does not exist'})
def doctorenter_report_view(request):
    doctorenter_reportviewdata = User.objects.filter(is_patient=True, Appoint=True, Approve=True, dFname=request.user.username)
    return render(request, 'hosapp/doctor_patient_report.html', {'doctorenter_reportviewdata': doctorenter_reportviewdata})


def patient_download_their(request,username):
        user = User.objects.get(username=username)
        number_of_days_spent = (timezone.now().date() - user.Admit_date).days
        context = {'report': user, 'day': number_of_days_spent, 'timezone': timezone} 
        return render(request,'hosapp/patient_download_their_bill.html',context)

