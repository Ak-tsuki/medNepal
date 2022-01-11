from django.shortcuts import render, redirect
from accounts.models import Patient
from admins.models import Medicine
from .models import Cart
from django.contrib import messages

# Create your views here.
def patient_homepage(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)
    context = {
        'patient':patient,
        'user':user
    }   
    return render(request, 'patients/homepage.html',context)

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
