from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserForm  # Import LoginForm and CustomUserForm from your forms.py

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # saves user and automatically hashes password1
            return redirect('login')  # or your desired success URL
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                elif user.role == 'distributor':
                    return redirect('distributor_dashboard')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def admin_dashboard(request):
    if request.user.is_authenticated and request.user.role == 'admin':
        return render(request, 'accounts/admin_dashboard.html')
    else:
        return redirect('login')
    
def distributor_dashboard(request):
    if request.user.is_authenticated and request.user.role == 'distributor':
        return render(request, 'accounts/distributor_dashboard.html')
    else:
        return redirect('login')