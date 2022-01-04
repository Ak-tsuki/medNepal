from django.db import models
from django.core import validators

# Create your models here.
class MedicineCategory(models.Model):
    med_category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_brief = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.med_category_name
        
# Model For Medicine
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=200)
    medicine_price = models.FloatField()
    medicine_image = models.FileField(upload_to='static/medicine_uploads', null = True)
    category = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE, null=True, related_name='category_medicine')
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.medicine_name