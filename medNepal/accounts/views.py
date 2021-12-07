from django.shortcuts import render
from .forms import LoginForm, CreateUserForm

# Create your views here.
def homepage(request):
    return render(request, 'accounts/homepage.html')


def login(request):
    context = {
        'form_login': LoginForm
    }
    return render(request, 'accounts/login.html',context)

def register_user(request):
    context = {
        'form_register': CreateUserForm,
    }
    return render(request, 'accounts/register.html', context)
