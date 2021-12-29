from django.shortcuts import render,redirect
from .forms import LoginForm, PatientSignUpForm, DoctorSignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User,Patient



from django.views.generic import CreateView

# Create your views here.
def homepage(request):
    return render(request, 'accounts/homepage.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/admins')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user name or password")
                return render(request, 'accounts/login.html', {'form_login': form})
    
    context = {
        'form_login': LoginForm
    }
    return render(request, 'accounts/login.html', context)



class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'accounts/signupPatient.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        return redirect('/login')
    

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'accounts/signupDoctor.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        return redirect('/login')



def logout_user(request):
    logout(request)
    return redirect('/login')



