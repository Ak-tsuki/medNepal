from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
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
    profile_pic = models.FileField(upload_to='static/patientProfile', default='static/default_user.png')
    gender = models.CharField(choices=gender_CHOICES,max_length=50)
    
    def __str__(self):
        return self.user.username


class Department(models.Model):
    DeptName = models.CharField(choices=department_CHOICES,max_length=100)
    deptPic = models.FileField(upload_to='static/uploads')
    description = RichTextField(blank=True, null=True)
    appointmentFee = models.IntegerField()

    def __str__(self):
        return self.DeptName

    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    profile_pic = models.FileField(upload_to='static/doctorProfile', default='static/default_user.png')
    departmentName = models.CharField(choices=department_CHOICES, max_length=100)
    hospitalName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username


