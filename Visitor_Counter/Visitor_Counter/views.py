from django.shortcuts import render

    
def visitor(request):
    # Initialize the visitor count in the session if it doesn't exist
    count = request.session.get('visitor', 0)  # Get the current count from the session, default to 0
    count += 1
    request.session['visitor'] = count  # Update the session with the new count
    return render(request, 'index.html', {'count': count})