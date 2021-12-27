from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .filters import *
from accounts.models import Doctor, Patient
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
    user_all = User.objects.all()
    users = user_all.filter(is_doctor=1)
    user_filter = UserFilter(request.GET, queryset=users)
    user_final = user_filter.qs

    context = {
        'users': user_final,
        'user_filter': user_filter,
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