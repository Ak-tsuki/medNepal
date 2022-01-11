from django.urls import path
from . import views

urlpatterns = [
    # doctor main dashboard or homapage
    # path('', views.patient_homepage),
    path('add_to_cart/<int:medicine_id>', views.add_to_cart),
    path('mycart', views.show_cart_items, name='show_cart_items'),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
]