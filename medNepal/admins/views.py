from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from patients.forms import LabTest_Form

from patients.models import LabTest
from .filters import *
from accounts.models import Doctor, Patient, Department
from accounts.forms import DepartmentForm
from .forms import LabReportForm, MedicineCategoryForm, MedicineForm
from .models import MedicineCategory, Medicine
from django.contrib import messages
import os
# Create your views here.
User = get_user_model()

def admin_dashboard(request):
    users = User.objects.all()
    doctor_count = users.filter(is_doctor=1).count()
    patient_count = users.filter(is_patient=1).count()
    admin_count = users.filter(is_staff=1).count()
    labtest = LabTest.objects.all().count()

    context = {
        'doctor': doctor_count,
        'patient': patient_count,
        'admin': admin_count,
        'labtest':labtest
    }

    return render(request, 'admins/homepage.html', context)


def get_doctor(request):
    user_all = Doctor.objects.all()
    context = {
        'users': user_all,
    }
    return render(request, 'admins/show_doctor.html', context)


def get_patient(request):
    user_all = User.objects.all()
    users = user_all.filter(is_patient=1)
    user_filter = UserFilter(request.GET, queryset=users)
    user_final = user_filter.qs

    context = {
        'users': user_final,
        'user_filter': user_filter,
    }

    return render(request, 'admins/show_patient.html', context)

def get_admin(request):
    users_all = User.objects.all()
    admins = users_all.filter(is_staff=1)


    context = {
        'admins': admins,
    }

    return render(request, 'admins/show_admin.html', context)




def post_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Posted successfully")
            return redirect('/admins/get_department')
        else:
            messages.add_message(request, messages.ERROR, "Unable to post successfully")
            return render(request, 'admins/post_department.html', {'form_department': form})

    context = {
        'form_department': DepartmentForm,
        'activate_post_department': 'active'
    }
    return render(request, 'admins/post_department.html', context)



def get_department(request):
    department = Department.objects.all().order_by('-id')

    context = {
        'files': department,
    }
    return render(request, 'admins/get_department.html', context)



def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    os.remove(department.deptPic.path)
    messages.add_message(request, messages.SUCCESS, "Succeccfully deleted")
    return redirect('/admins/get_department')



def update_department(request, department_id):
    department = Department.objects.get(id=department_id)

    if request.method == 'POST':
        if request.FILES.get('deptPic'):
            os.remove(department.deptPic.path)
            
        form = DepartmentForm(request.POST, request.FILES, instance=department)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Updated successfully")
            return redirect('/admins/get_department')
        else:
            messages.add_message(request, messages.ERROR, "Unable to update successfully")
            return render(request, 'admins/update_department.html', {'form_department': form})

    context = {
        'form_department': DepartmentForm(instance=department),
    }
    return render(request, 'admins/update_department.html', context)



def post_medicine_category(request):
    if request.method == 'POST':
        form = MedicineCategoryForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Medicine Category Added Successfully")
            return redirect('/admins/get_medicine_category')
        else:
            messages.add_message(request, messages.ERROR, "Unable to Add Medicine Category")
            return render(request, 'admins/post_medicine_category.html', {'form_medicine_category': form})

    context = {
        'form_medicine_category': MedicineCategoryForm,
        # 'activate_post_department': 'active'
    }
    return render(request, 'admins/post_medicine_category.html', context)

def get_medicine_category(request):
    medicine_category = MedicineCategory.objects.all().order_by('-id')

    context = {
        'files': medicine_category,
    }
    return render(request, 'admins/get_medicine_category.html', context)


def delete_medicine_category(request, medicine_category_id):
    medicine_category = MedicineCategory.objects.get(id=medicine_category_id)
    medicine_category.delete()
    messages.add_message(request, messages.SUCCESS, "Succeccfully deleted")
    return redirect('/admins/get_medicine_category')

def update_medicine_category(request, medicine_category_id):
    medicine_category = MedicineCategory.objects.get(id=medicine_category_id)

    if request.method == 'POST':            
        form = MedicineCategoryForm(request.POST, request.FILES, instance=medicine_category)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Updated successfully")
            return redirect('/admins/get_medicine_category')
        else:
            messages.add_message(request, messages.ERROR, "Unable to update successfully")
            return render(request, 'admins/update_medicine_category.html', {'form_medicine_category': form})

    context = {
        'form_medicine_category': MedicineCategoryForm(instance=medicine_category),
    }
    return render(request, 'admins/update_medicine_category.html', context)

def post_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Medicine Added Successfully")
            return redirect('/admins/get_medicine')
        else:
            messages.add_message(request, messages.ERROR, "Unable to Add Medicine")
            return render(request, 'admins/post_medicine.html', {'form_medicine': form})

    context = {
        'form_medicine': MedicineForm,
        # 'activate_post_department': 'active'
    }
    return render(request, 'admins/post_medicine.html', context)

def get_medicine(request):
    medicine = Medicine.objects.all().order_by('-id')

    context = {
        'files': medicine,
    }
    return render(request, 'admins/get_medicine.html', context)

def delete_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicine.delete()
    os.remove(medicine.medicine_image.path)
    messages.add_message(request, messages.SUCCESS, "Succeccfully deleted")
    return redirect('/admins/get_medicine')

def update_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == 'POST':
        if request.FILES.get('medicine_image'):
            os.remove(medicine.medicine_image.path)
            
        form = MedicineForm(request.POST, request.FILES, instance=medicine)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Updated successfully")
            return redirect('/admins/get_medicine')
        else:
            messages.add_message(request, messages.ERROR, "Unable to update successfully")
            return render(request, 'admins/update_medicine.html', {'form_medicine': form})

    context = {
        'form_medicine': MedicineForm(instance=medicine),
    }
    return render(request, 'admins/update_medicine.html', context)


def show_book_labtest(request):
    labtest = LabTest.objects.all()
    context = {
        'labtests': labtest,
    }
    return render(request, 'admins/show_book_labtest.html', context)

def update_labtest(request,labtest_id):
    labtest = LabTest.objects.get(id=labtest_id)
    if request.method == 'POST':
        form = LabTest_Form(request.POST, request.FILES, instance=labtest)  
        if form.is_valid():
            form.save()
            return redirect('/admins/show_book_labtest')
            
    context = {
        'form_labtest': LabTest_Form(instance=labtest)
    }
    return render(request, 'admins/update_labtest.html',context)

def accept_labtest(request, labtest_id):
    labtest = LabTest.objects.get(id=labtest_id)
    labtest.status = True
    labtest.save()
    messages.add_message(request, messages.SUCCESS, 'labtest accepted  Successfully')
    return redirect('/admins/show_book_labtest')

def upload_labreport(request, labtest_id):
    labtest = LabTest.objects.get(id=labtest_id)
    if request.method == 'POST':
        form = LabReportForm(request.POST, request.FILES)  
        if form.is_valid():
            report = form.cleaned_data.get('report')
            labtest.report = report
            labtest.save()
            return redirect('/admins/show_book_labtest')
            
    context = {
        'form_labreport': LabReportForm()
    }
    return render(request, 'admins/upload_labreport.html',context)

    
