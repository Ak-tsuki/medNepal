from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from .models import *



class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PatientSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    age = forms.CharField(required=True)
    profilePic=forms.FileField(required=True)
    gender = forms.ChoiceField(choices=gender_CHOICES, widget=forms.Select(), required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.firstname=self.cleaned_data.get('firstname')
        patient.lastname=self.cleaned_data.get('lastname')
        patient.phone=self.cleaned_data.get('phone')
        patient.address=self.cleaned_data.get('address')
        patient.age=self.cleaned_data.get('age')
        patient.profile_pic=self.cleaned_data.get('profilePic')
        patient.gender=self.cleaned_data.get('gender')
        patient.save()
        return patient     


class DoctorSignUpForm(UserCreationForm):
   
    email=forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    phone=forms.CharField(required=True)
    address=forms.CharField(required=True)
    profilePic=forms.FileField(required=True)
    departmentName = forms.ChoiceField(choices=department_CHOICES, widget=forms.Select(), required=True)
    hospitalName = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.firstname=self.cleaned_data.get('firstname')
        doctor.lastname=self.cleaned_data.get('lastname')
        doctor.phone=self.cleaned_data.get('phone')
        doctor.address=self.cleaned_data.get('address')
        doctor.profile_pic=self.cleaned_data.get('profilePic')
        doctor.departmentName=self.cleaned_data.get('departmentName')
        doctor.hospitalName=self.cleaned_data.get('hospitalName')
        doctor.save()
        return doctor  
    
