from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('show_user', views.get_user)
]