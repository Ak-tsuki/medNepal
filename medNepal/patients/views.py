import os
from django.shortcuts import render, redirect
from accounts.models import Patient
from admins.models import Medicine
from .models import Cart
from .forms import Profile_Form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

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
