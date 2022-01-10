from django.urls import path
from . import views

urlpatterns = [
    # doctor main dashboard or homapage
    path('', views.patient_homepage),
]