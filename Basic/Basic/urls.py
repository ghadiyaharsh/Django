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
    path('', views.homepage, name='homepage'),  # direct open the homepage
    path('about-us/', views.about_us, name='about-us'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('course/<slug:course_id>/', views.coursedetail, name='coursedetail'),
    path('skill/', views.skills, name='skills'),
    path('student/', views.student, name='student'),
    path('registration/', views.registration, name='registration'),
    path('base/',views.base, name='base'),  # this is the URL pattern for the base template
]
# about-us is a link and views.aboutUS is the function that will be called when the user visits that link
# this is the URL pattern for the about us page
