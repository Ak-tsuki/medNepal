from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login),
    path('register', views.register_user)
]