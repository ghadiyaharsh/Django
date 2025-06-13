from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})