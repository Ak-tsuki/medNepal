from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

department_CHOICES = [
    ('Anesthesiologists', 'Anesthesiologists'),
    ('Cardiologists', 'Cardiologists'),
    ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
    ('WednCritical Care Medicine Specialistsesday', 'WednCritical Care Medicine Specialistsesday'),
    ('Dermatologists', 'Dermatologists'),
    ('Endocrinologists', 'Endocrinologists'),
    ('Gastroenterologists', 'Gastroenterologists'),
]


gender_CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]



class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=gender_CHOICES,max_length=50)
    
    def __str__(self):
        return self.user.username
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    departmentName = models.CharField(choices=department_CHOICES,max_length=100)
    
    def __str__(self):
        return self.user.username

