from django.shortcuts import render,redirect
from .forms import LoginForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def homepage(request):
    return render(request, 'accounts/homepage.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                if not user.is_staff:
                    #login(request, user)
                    return redirect('/register')
                elif user.is_staff:
                    #login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user name or password")
                return render(request, 'accounts/login.html', {'form_login': form})

    context = {
        'form_login': LoginForm
    }
    return render(request, 'accounts/login.html',context)

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User registered successfully")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong")
            return render(request, 'accounts/register.html', {'form_register': form})
    
    context = {
        'form_register': CreateUserForm,
    }
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')