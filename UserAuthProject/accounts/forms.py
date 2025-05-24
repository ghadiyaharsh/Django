from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True, max_length=254, help_text='Enter the email associated with your account.')
    
class verifyOTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, help_text='Enter the OTP sent to your email.')        
    
    
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    