from django import forms
from django.forms import ModelForm
from accounts.models import Doctor

class Profile_Form(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user']