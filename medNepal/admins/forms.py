from django import forms
from .models import MedicineCategory, Medicine
from django.forms import ModelForm


class MedicineCategoryForm(ModelForm):
    class Meta:
        model = MedicineCategory
        fields = '__all__'
class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'