from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login_user),
    path('get_profile', views.get_profile),
    path('signup/patient', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('signup/doctor', views.DoctorSignUpView.as_view(), name='doctor_signup')
]