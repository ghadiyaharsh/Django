from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserForm, ForgotPasswordForm, verifyOTPForm, ResetPasswordForm  # Import all forms including ResetPasswordForm from your forms.py
from .models import CustomUser  # Import CustomUser from your models.py
from django.core.mail import send_mail
from django.conf import settings
import random


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
    


def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                otp = random.randint(100000, 999999)
                request.session['reset_email'] = email
                request.session['otp'] = str(otp)
                
                # Send OTP via email
                send_mail(
                    'Your OTP Code',
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                
                return redirect('verify_otp')
            else:
                form.add_error('email', 'Email not found')
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgot_password.html', {'form': form})
   
   
def verify_otp_view(request):
    if request.method == 'POST':
        form = verifyOTPForm(request.POST)
        if form.is_valid():
            input_otp = form.cleaned_data['otp']
            session_otp = request.session.get('otp')
            if input_otp == session_otp:
                return redirect('reset_password')
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = verifyOTPForm()
    return render(request, 'accounts/verify_otp.html', {'form': form})
 
def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            p1 = form.cleaned_data['new_password']
            p2 = form.cleaned_data['confirm_password']
            if p1 != p2:
                form.add_error('confirm_password', 'Passwords do not match')
            else:
                email = request.session.get('reset_email')
                user = CustomUser.objects.get(email=email)
                user.set_password(p1)
                user.save()
                # Clear session
                request.session.flush()
                return redirect('login')
    else:
        form = ResetPasswordForm()
    return render(request, 'accounts/reset_password.html', {'form': form})
 