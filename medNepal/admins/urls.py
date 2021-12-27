from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('show_doctor', views.get_doctor),
    path('show_patient', views.get_patient),
]