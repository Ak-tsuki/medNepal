from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # doctor main dashboard or homapage
    # path('', views.patient_homepage),
    path('add_to_cart/<int:medicine_id>', views.add_to_cart),
    path('mycart', views.show_cart_items, name='show_cart_items'),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    
    path('book_appointment/<int:doctor_id>', views.book_appointment),
    path('show_book_appointment', views.show_book_appointment, name='show_book_appointment'),
    path('remove_book_appointment/<int:appointment_id>', views.remove_book_appointment),
    
    path('book_labtest', views.book_labtest),
    path('show_book_labtest', views.show_book_labtest, name='show_book_labtest'),
    
    path('get_profile', views.get_profile),
    path('update_profile', views.update_profile),
    path('password_change', views.password_change),
    
    path('inbox/', views.ListThreads.as_view(),name='inbox'),
    
    path('inbox/create-thread-view/<int:d_id>', views.createThread, name='create-thread-view'),
    
    path('inbox/<int:pk>/', views.ThreadView.as_view(), name='thread'),
    path('indox/<int:pk>/create-message/', views.CreateMessage.as_view(), name='create-message'),
]