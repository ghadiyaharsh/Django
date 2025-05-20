from django.shortcuts import render

# Create your views here.
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Feedback.objects.create(name=name, email=email, message=message)
    return render(request, 'feedback.html')  
    return render(request, 'thanks.html')     
    

def thanks(request):
    return render(request, 'thanks.html')