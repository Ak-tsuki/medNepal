from django.db import models
from django.core.validators import *
from django.core import validators
# from django.contrib.auth.models import User
from accounts.models import User
from admins.models import Medicine


# Create your models here.
# Model For Cart
class Cart(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

