from django.urls import path
from . import views

urlpatterns = [
    # doctor main dashboard or homapage
    path('', views.doctor_dashboard),
    path('get_profile', views.get_profile),
    path('update_profile', views.update_profile),
    path('password_change', views.password_change),
    
    path('show_appointment', views.show_appointment, name='show_appointment'),
    path('accept_appointment/<int:appointment_id>', views.accept_appointment),
    path('remove_appointment/<int:appointment_id>', views.remove_appointment),
    path('update_appointment/<int:appointment_id>', views.update_appointment, name='update_appointment'), 
    
    path('inbox/', views.ListThreads.as_view(),name='inbox_doctor'),
    path('inbox/<int:pk>/', views.ThreadView.as_view(), name='thread_doctor'),
    path('indox/<int:pk>/create-message/', views.CreateMessage.as_view(), name='create-message_doctor'),
    
]