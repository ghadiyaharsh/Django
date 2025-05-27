from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title': 'Home Page',
        'course_name': ['Python', 'Java', 'C++', 'JavaScript'],
        'number':[10, 20, 30, 40],
        #'number': [1, 2, 3, 4],
        'course_duration': [
            {'name': 'Python', 'duration': '3 months'},
            {'name': 'Java', 'duration': '4 months'},
            {'name': 'C++', 'duration': '5 months'},
            {'name': 'JavaScript', 'duration': '6 months'},
        ]
         
    }
    return render(request, "index.html", data)

def about_us(request):
    data3 = {
        'team_members': [
            {'name': 'Alice', 'role': 'Developer'},
            {'name': 'Bob', 'role': 'Designer'},
            {'name': 'Charlie', 'role': 'Project Manager'},
            {'name': 'Diana', 'role': 'Tester'}
        ],
    }
    return render(request, "about-us.html",data3)

def home(request):
    return HttpResponse("Welcome to the home page")

def contact(request):
    return HttpResponse("Welcome to the contact page")

def course(request):
    return HttpResponse("Welcome to the course page")

def coursedetail(request, course_id):
    return HttpResponse(f"Welcome to the course page with course id: {course_id}")

def skills(request):
    return HttpResponse("Welcome to the skill page")

def student(request):
    return HttpResponse("Welcome to the student page")

def registration(request):
    data1 = {
        'title': 'Registration Form',
    }
    return render(request, "registration.html", data1)
