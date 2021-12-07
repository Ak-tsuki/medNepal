from django.shortcuts import render

# =====================Article Page Part========================================
def article(request):
    return render(request, 'features/article.html')

# =====================Doctor Page Part========================================
def doctorpage(request):
    return render(request, 'features/doctorpage.html')

# =====================Pharmacy Page Part========================================
def pharmacy(request):
    return render(request, 'features/pharmacy.html')

# =====================SearchDoctor Page Part========================================
def searchdoctor(request):
    return render(request, 'features/searchdoctor.html')



