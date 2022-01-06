from django.urls import path
from . import views

urlpatterns = [
    # doctor main dashboard or homapage
    path('', views.doctor_dashboard),
    path('get_profile', views.get_profile),
]