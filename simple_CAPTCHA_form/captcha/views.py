from django.shortcuts import render,redirect
from .form import CaptchaForm

# Create your views here.

def captcha_view(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            return redirect('success')
    else:
        form = CaptchaForm()
    # {'form': form} is a context dictionary.
    # It passes the form instance to the template as the variable 'form'.
    # In the template, you can access this form using {{ form }}.
    return render(request, 'captcha.html', {'form': form})


def success_view(request):
    return render (request, 'success.html')