from importlib.metadata import requires
from operator import mod
from pyexpat import model
from time import timezone
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
    status = models.BooleanField(default=False)
    booked_date = models.DateTimeField(auto_now_add=True)
    

class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    labtest_Date_Time = models.DateTimeField()
    status = models.BooleanField(default=False)
    booked_date = models.DateTimeField(auto_now_add=True)
    report = models.FileField(upload_to='static/patientLabreport', null = True)
    
    
# class Labreport(models.Model):
#     labtest = models.ForeignKey(LabTest,on_delete=models.CASCADE)
    
#     uploadeddate = models.DateTimeField(auto_now_add=True, null=True)


class ThreadModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    
class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

# Model For Food Ordering
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
    )
    medicine = models.ForeignKey(Medicine, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    payment_method = models.CharField(max_length=200, choices=PAYMENT, null=True)
    payment_status = models.BooleanField(default=False, null=True, blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    contact_address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)