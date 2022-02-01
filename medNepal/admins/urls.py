from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('show_doctor', views.get_doctor),
    path('show_patient', views.get_patient),
    path('show_admin', views.get_admin),
    
    path('post_department', views.post_department, name='post_department'),
    path('get_department', views.get_department, name='get_department'),
    path('delete_department/<int:department_id>', views.delete_department, name='delete_department'),
    path('update_department/<int:department_id>', views.update_department),

    path('post_medicine_category', views.post_medicine_category, name='post_medicine_category'),
    path('get_medicine_category', views.get_medicine_category, name='get_medicine_category'),
    path('delete_medicine_category/<int:medicine_category_id>', views.delete_medicine_category, name='delete_medicine_category'),
    path('update_medicine_category/<int:medicine_category_id>', views.update_medicine_category),

    path('post_medicine', views.post_medicine, name='post_medicine'),
    path('get_medicine', views.get_medicine, name='get_medicine'),
    path('delete_medicine/<int:medicine_id>', views.delete_medicine, name='delete_medicine'),
    path('update_medicine/<int:medicine_id>', views.update_medicine),
    
    path('show_book_labtest', views.show_book_labtest, name='show_book_labtest'),
    path('update_labtest/<int:labtest_id>', views.update_labtest, name='update_labtest'),
    path('accept_labtest/<int:labtest_id>', views.accept_labtest, name='accept_labtest'),
    path('upload_labreport/<int:labtest_id>', views.upload_labreport, name='upload_labreport'),   
]