from django import forms

from patients.models import LabTest
from .models import Article, MedicineCategory, Medicine
from django.forms import DateTimeInput, ModelForm


class MedicineCategoryForm(ModelForm):
    class Meta:
        model = MedicineCategory
        fields = '__all__'
        
class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        
class LabReportForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ['report']
        
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
