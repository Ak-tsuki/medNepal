import os
from django.shortcuts import render,redirect
from django.contrib import messages

from accounts.models import Doctor
from .forms import Profile_Form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def doctor_dashboard(request):
    user = request.user
    doctor = Doctor.objects.get(user_id=user.id)
    context = {
        'doctor':doctor,
        'user':user
    }   
    return render(request, 'doctors/homepage.html',context)


def get_profile(request):
    user = request.user
    doctor = Doctor.objects.get(user_id=user.id)
    context = {
        'doctor':doctor,
        'user':user
    }   
    return render(request, 'doctors/get_profile.html', context)


def update_profile(request):
    user = request.user
    doctor = Doctor.objects.get(user_id=user.id)
    if request.method == 'POST':
        if request.FILES.get('profile_pic'):
            os.remove(doctor.profile_pic.path)

        form = Profile_Form(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile Updated successfully")
            return redirect('/doctors/get_profile')
        
    context = {
        'profile': doctor,
        'form': Profile_Form(instance=doctor),
        'activate_profile': 'active'
    }
    return render(request, 'doctors/update_profile.html', context)


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/doctors/get_profile')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'doctors/password_change.html', {'password_change_form': form})

    context = {
        'password_change_form': PasswordChangeForm(request.user),
    }
    return render(request, 'doctors/password_change.html', context)
