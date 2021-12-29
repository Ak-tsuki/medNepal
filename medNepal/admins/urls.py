from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('show_doctor', views.get_doctor),
    path('show_patient', views.get_patient),
    
    path('post_department', views.post_department, name='post_department'),
    path('get_department', views.get_department, name='get_department'),
    path('delete_department/<int:department_id>', views.delete_department, name='delete_department'),
    path('update_department/<int:department_id>', views.update_department),
    
]