from django.shortcuts import render
from accounts.models import Department, Doctor

# =====================Article Page Part========================================
def article(request):
    return render(request, 'features/article.html')

# =====================Doctor Page Part========================================
def doctorpage(request, d_id):
    doctor = Doctor.objects.get(user_id=d_id)
    department = Department.objects.get(DeptName=doctor.departmentName)
    
    context={
        'doctor':doctor,
        'department':department
    }
    
    return render(request, 'features/doctorpage.html',context)

# =====================Pharmacy Page Part========================================
def pharmacy(request):
    return render(request, 'features/pharmacy.html')

# =====================SearchDoctor Page Part========================================
def searchdoctor(request):
    doctor_all = Doctor.objects.all()

    context = {
        'doctors': doctor_all,
    }
    return render(request, 'features/searchdoctor.html',context)



