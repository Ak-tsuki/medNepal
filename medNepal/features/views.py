from django.shortcuts import render
from accounts.models import Department, Doctor
from admins.models import MedicineCategory,Medicine
from features.filters import DoctorFilter

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
    pharmacy_category_all= MedicineCategory.objects.all()
    # pharmacy_all = Medicine.objects.all()
    context = {
        'medicine_category': pharmacy_category_all,
        # 'medicines': pharmacy_all,
    }
    return render(request, 'features/pharmacy.html',context)

# =====================SearchDoctor Page Part========================================
def searchdoctor(request):
    doctor_all = Doctor.objects.all()
    doctor_filter = DoctorFilter(request.GET, queryset=doctor_all)
    doctor_final = doctor_filter.qs
    context = {
        'doctors': doctor_final,
        'doctor_filter':doctor_filter
    }
    return render(request, 'features/searchdoctor.html',context)



