from email import message
from pyexpat import model
from django import forms
from django.forms import ModelForm, widgets
from accounts.models import Patient
from .models import Appointment, Order

class Profile_Form(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']
        
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'        

class Appointment_Form(ModelForm):
    class Meta:
        widgets = {'appointment_Date_Time' : DateTimeInput()}
        model = Appointment
        fields = ['appointment_Date_Time']
        

# class ThreadForm(forms.Form):
#     username = forms.CharField(label='',max_length=100)
     
class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']
