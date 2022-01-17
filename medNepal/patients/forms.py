from django import forms
from django.forms import ModelForm
from accounts.models import Patient

class Profile_Form(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']