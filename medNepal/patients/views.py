from email import message
from genericpath import exists
import os
from django.db.models import Q
from django.shortcuts import render, redirect
from accounts.models import Doctor, Patient, Department, User
from admins.models import Medicine
from .models import Appointment, Cart, MessageModel, ThreadModel
from .forms import MessageForm, Profile_Form,Appointment_Form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
# def patient_homepage(request):
#     user = request.user
#     patient = Patient.objects.get(user_id=user.id)
#     context = {
#         'patient':patient,
#         'user':user
#     }   
#     return render(request, 'patients/homepage.html',context)

#Add To Cart
def add_to_cart(request, medicine_id):
    user = request.user
    medicine = Medicine.objects.get(id=medicine_id)
    check_item_presence = Cart.objects.filter(user=user, medicine=medicine)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Medicine Is Already In The Cart.')
        return redirect("/patients/mycart")

    else:
        cart = Cart.objects.create(medicine=medicine, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Medicine Added To Cart')
            return redirect("/patients/mycart")
        else:
            messages.add_message(request, messages.ERROR, 'Unable To Add Medicine To Cart')

def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {
        'items': items,
    }
    return render(request, 'patients/my_cart.html', context)

def remove_cart_item(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Cart Medicine Removed Successfully')
    return redirect('/patients/mycart')


def book_appointment(request, doctor_id):
    user = request.user
    patient = Patient.objects.get(user_id=user.id) 
    doctor = Doctor.objects.get(user_id=doctor_id)
    department = Department.objects.get(DeptName=doctor.departmentName)

    if request.method == 'POST':
        form = Appointment_Form(request.POST)  
        if form.is_valid():
            appointment = Appointment.objects.create(patient = patient,doctor = doctor, appointment_Date_Time = request.POST.get('appointment_Date_Time'))
            
            if appointment:
                messages.add_message(request, messages.SUCCESS, 'Appointment Succesfull')
                return redirect('/patients/show_book_appointment')
            
    context = {
        'form_Appointment': Appointment_Form,
        'doctor':doctor,
        'department':department
    }
    return render(request, 'patients/book_appointment.html',context)

def show_book_appointment(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id) 
    appointment = Appointment.objects.filter(patient=patient)
    context = {
        'appointments': appointment,
    }
    return render(request, 'patients/show_book_appointment.html', context)

def remove_book_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, 'Booked appointment Removed Successfully')
    return redirect('/patients/show_book_appointment')


def get_profile(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)
    context = {
        'patient':patient,
        'user':user
    }   
    return render(request, 'patients/get_profile.html', context)


def update_profile(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)
    if request.method == 'POST':
        if request.FILES.get('profile_pic'):
            os.remove(patient.profile_pic.path)

        form = Profile_Form(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile Updated successfully")
            return redirect('/patients/get_profile')
        
    context = {
        'profile': patient,
        'form': Profile_Form(instance=patient),
        'activate_profile': 'active'
    }
    return render(request, 'patients/update_profile.html', context)


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
    return render(request, 'patients/password_change.html', context)


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    
        context = {
            'threads':threads
        }
        
        return render(request,'patients/inbo.html', context)
    
# class CreateThread(View):
#     def get(self, request, *args, **kwargs):
#         form = ThreadForm()
        
#         context = {
#             'form': form

#         }
#         return render(request, 'patients/createThread.html', context)
        
#     def post(self, request, *args, **kwargs):
#         form = ThreadForm(request.POST)
        
#         username = request.POST.get('username')
        
#         try:
#             receiver = User.objects.get(username=username)
#             if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
#                 thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
#                 return redirect('thread', pk=thread.pk)
#             elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
#                 thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
#                 return redirect('thread', pk=thread.pk)
            
#             if form.is_valid():
#                 thread = ThreadModel(
#                     user=request.user,
#                     receiver=receiver
#                 )
#                 thread.save()
                
#                 return redirect('thread', pk=thread.pk)
#         except:
#             return redirect('create-thread')
        

def createThread(request, d_id):
        receiver = User.objects.get(id=d_id)   
        
        if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
            thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
            return redirect('thread', pk=thread.pk)
        
        else:
            thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
            thread.save()
                
            return redirect('thread', pk=thread.pk)




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
        return render(request, 'patients/thread.html',context)


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
        return redirect('thread', pk=pk)