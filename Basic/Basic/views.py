from django.http import HttpResponse 
#this is a built-in Django module that allows us to return HTTP responses

def aboutUS(request): #this is a function that takes a request and returns an HTTP response
    #this function is called when the user visits the about us page

    return HttpResponse("welcome to the about us page")
#this function returns an HTTP response with the content of the about us page

def home(request): #this is a function that takes a request and returns an HTTP response
     
   return HttpResponse("welcome to the home page")

def contact(request): #this is a function that takes a request and returns an HTTP response
    return HttpResponse("welcome to the contact page")  
