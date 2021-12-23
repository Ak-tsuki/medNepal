from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .filters import *
# Create your views here.
User = get_user_model()

def admin_dashboard(request):
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()

    context = {
        'user': user_count,
        'admin': admin_count
    }

    return render(request, 'admins/homepage.html', context)


def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    user_filter = UserFilter(request.GET, queryset=users)
    user_final = user_filter.qs

    context = {
        'users': user_final,
        'user_filter': user_filter,
    }

    return render(request, 'admins/show_user.html', context)
