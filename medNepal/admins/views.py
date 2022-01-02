from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .filters import *
from accounts.models import Doctor, Patient, Department
from accounts.forms import DepartmentForm
from django.contrib import messages
import os
# Create your views here.
User = get_user_model()

def admin_dashboard(request):
    users = User.objects.all()
    doctor_count = users.filter(is_doctor=1).count()
    patient_count = users.filter(is_patient=1).count()
    admin_count = users.filter(is_staff=1).count()

    context = {
        'doctor': doctor_count,
        'patient': patient_count,
        'admin': admin_count
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




