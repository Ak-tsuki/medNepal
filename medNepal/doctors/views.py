import os
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View
from django.db.models import Q

from accounts.models import Doctor
from patients.forms import MessageForm
from patients.models import Appointment, MessageModel, ThreadModel
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




def show_appointment(request):
    user = request.user
    doctor = Doctor.objects.get(user_id=user.id) 
    appointment = Appointment.objects.filter(doctor=doctor)
    context = {
        'appointments': appointment,
    }
    return render(request, 'doctors/show_appointment.html', context)

def accept_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = True
    appointment.save()
    messages.add_message(request, messages.SUCCESS, 'Appointment accepted  Successfully')
    return redirect('/doctors/show_appointment')

def remove_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, 'Booked appointment Removed Successfully')
    return redirect('/doctors/show_appointment')



class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    
        context = {
            'threads':threads
        }
        
        return render(request,'doctors/inbo.html', context)
    
        


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list':message_list
        }
        
        return render(request, 'doctors/thread.html',context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):  
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver 
            
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )
        
        message.save()
        return redirect('thread_doctor', pk=pk)