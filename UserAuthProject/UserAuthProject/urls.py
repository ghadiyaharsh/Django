"""
URL configuration for UserAuthProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views  # Adjust import to match your project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('distributor_dashboard/', views.distributor_dashboard, name='distributor_dashboard'),
    path('', views.register_view, name='register'),
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),
    path('verify_otp/', views.verify_otp_view, name='verify_otp'),
    path('reset_password/', views.reset_password_view, name='reset_password'),

]
