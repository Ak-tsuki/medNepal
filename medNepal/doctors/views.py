from django.shortcuts import render

from accounts.models import Doctor

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
