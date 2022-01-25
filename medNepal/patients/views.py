from email import message
from genericpath import exists
import os
from django.db.models import Q
from django.shortcuts import render, redirect
from accounts.models import Doctor, Patient, Department, User
from admins.models import Medicine
from .models import Appointment, Cart, MessageModel, ThreadModel, Order
from .forms import MessageForm, Profile_Form,Appointment_Form, OrderForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
import requests as req

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

def order_form(request, medicine_id, cart_id):
    user = request.user
    medicine = Medicine.objects.get(id=medicine_id)
    cart_item = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = medicine.medicine_price
            total_price = int(quantity) * int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(medicine=medicine,
                                         user=user,
                                         quantity=quantity,
                                         total_price=total_price,
                                         contact_no=contact_no,
                                         contact_address=contact_address,
                                         status="Pending",
                                         payment_method=payment_method,
                                         payment_status=False
                                         )
            if order:
                # messages.add_message(request, messages.SUCCESS, 'Item Ordered. Continue Payment for Verification')
                # cart_item.delete()
                context = {
                    'order': order,
                    'cart': cart_item,
                }
                return render(request, 'patients/esewa_payment.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'patients/order_form.html', {'order_form': form})
    context = {
        'order_form': OrderForm
    }
    return render(request, 'patients/order_form.html', context)

def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/patients/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/patients/mycart')

def my_order(request):
    # cart = Cart.objects.all()
    # cart_count = cart.count()
    # wishlist = Wishlist.objects.all()
    # wishlist_count = wishlist.count()
    user = request.user
    items = Order.objects.filter(user=user, payment_status=True).order_by('-id')
    context = {
        'items': items,
        'activate_myorders': 'active',
        # 'count': cart_count,
        # 'count_list': wishlist_count,

    }
    return render(request, 'patients/my_order.html', context)

def get_order(request):
    order = Order.objects.all().order_by('-id')
    context = {
        'order': order,
        'activate_order': 'active',
    }
    return render(request, 'patients/get_order.html', context)

def deleteOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.add_message(request, messages.SUCCESS, 'Order has been deleted Successfully')
    return redirect('/patients/get_order')

def updateOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Delivered'
    order.save()
    messages.add_message(request, messages.SUCCESS, 'Order Has Been Delivered Successfully')
    return redirect('/patients/get_order')