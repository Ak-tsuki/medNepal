from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login_user),
    path('logout', views.logout_user,name='logout'),
   
    path('signup/patient', views.PatientSignUpView.as_view(), name='patient_signup'),
    path('signup/doctor', views.DoctorSignUpView.as_view(), name='doctor_signup'),

    

]