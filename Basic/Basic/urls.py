"""
URL configuration for Basic project.

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
from Basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUS, name='aboutUS'), #this is the URL pattern for the about us page
    path('home/',views.home, name='home'), #this is the URL pattern for the home page
    path('contact/',views.contact, name='contact'), #this is the URL pattern for the contact page
]
#about -us is a link and views.aboutUS is the function that will be called when the user visits that link
#this is the URL pattern for the about us page
