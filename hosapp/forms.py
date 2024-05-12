from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from hosapp.models import User
import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>login and Sign UP of doctor,patientts,admin>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# /////////////////////////////////////////////////////////////Admin/////////////////////////
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username','password')


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalpha():
            raise forms.ValidationError("Username must contain only alphabetic characters.")
        return username

    class Meta:
        model = User
        fields = ('id', 'username','email','password1','password2','is_admin', 'is_doctor', 'is_patient')


#  ////////////////////////////////////////////Doctor???????????????????????????????       //////////////////
        

class Doctor_SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match("^[a-zA-Z]+$", username):
            raise forms.ValidationError("Username must contain only alphabetic characters.")
        return username

    class Meta:
        model = User
        fields = ('id', 'username','email','password1','password2', 'is_doctor')


class Doctor_LoginForm(forms.Form):
    username= forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username','password')

# //////////////////////////////////////Patients?????????????????????????????????????????????????????????????????????????????????
        
class Patient_SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match("^[a-zA-Z]+$", username):
            raise forms.ValidationError("Username must contain only alphabetic characters.")
        return username

    class Meta:
        model = User
        fields = ('id', 'username','email','password1','password2', 'is_patient')


class Patients_LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username','password')




# ...............................................................................................

class AddDoctorForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    Dphone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password1', 'dob', 'age', 'gender', 'address', 'Dphone', 'department', 'is_doctor')

class AddPatientForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    Problem_pat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password1', 'dob', 'age', 'gender', 'address', 'phone', 'Problem_pat', 'is_patient')

     