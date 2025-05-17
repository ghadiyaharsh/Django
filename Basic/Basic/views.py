from django.http import HttpResponse 
from django.shortcuts import render
#this is a built-in Django module that allows us to return HTTP responses




def homepage(request): 
    
    data = {
        # yaha se html page me show karne ke liye data variable create kiya hai key value pair
        'title': 'Home Page',
        'course_name': ['Python', 'Java', 'C++', 'JavaScript'],
        
        'course_duration': [
            {'name':'Python', 'duration' :'3 months'},
            {'name':'Java', 'duration': '4 months'},
            {'name': 'C++', 'duration': '5 months'},
            {'name': 'JavaScript', 'duration': '6 months'},
        ]
    }
    #this is a function that takes a request and returns an HTTP response
    #this function returns an HTTP response with the content of the homepage
    return render(request,"index.html",data) #this is a built-in Django function that returns an HTTP response

def aboutUS(request): 
    return HttpResponse("welcome to the about us page")
    
def home(request): 
     
   return HttpResponse("welcome to the home page")

def contact(request): #this is a function that takes a request and returns an HTTP response
    return HttpResponse("welcome to the contact page")  

def course(request): #this is a function that takes a request and returns an HTTP response
    return HttpResponse("welcome to the course page")

def coursedetail(request, course_id): #this is a function that takes a request and returns an HTTP response
    return HttpResponse("welcome to the course page with course id: " + str(course_id))


def skills(request):
   return HttpResponse("welcome to the skill page")

def student(request):
    return HttpResponse("welcome to the student page")

data1={
    'title':'ragistrationform',
}
def ragistrationform(request):
    return render(request,"ragistration.html",data1)