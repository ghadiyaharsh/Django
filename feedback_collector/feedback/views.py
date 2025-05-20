from django.shortcuts import render, redirect
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Feedback.objects.create(name=name, email=email, message=message)
            return redirect('thanks')  # Redirects to thank-you page

    return render(request, 'feedback.html')

def thanks(request):
    return render(request, 'thanks.html')
