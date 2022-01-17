from importlib.metadata import requires
from django.db import models
from django.core.validators import *
from django.core import validators
# from django.contrib.auth.models import User
from accounts.models import Doctor, Patient, User
from admins.models import Medicine


# Create your models here.
# Model For Cart
class Cart(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_Date_Time = models.DateTimeField()
    status = models.TextField()
    booked_date = models.DateTimeField(auto_now_add=True)