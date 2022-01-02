from django.urls import path
from . import views

urlpatterns = [
    # Article Page Path
    path('article', views.article, name='article'),
    # Doctor Page Path
    path('doctorpage/<int:d_id>', views.doctorpage),
    # Pharmacy Page Path
    path('pharmacy', views.pharmacy),
    # SearchDoctor Page Path
    path('searchdoctor', views.searchdoctor),
]
