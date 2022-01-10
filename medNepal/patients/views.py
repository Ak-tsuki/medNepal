from django.shortcuts import render

from accounts.models import Patient

# Create your views here.
def patient_homepage(request):
    user = request.user
    patient = Patient.objects.get(user_id=user.id)
    context = {
        'patient':patient,
        'user':user
    }   
    return render(request, 'patients/homepage.html',context)