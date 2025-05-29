from django.shortcuts import render, redirect
from .forms import TaskForm  # Import the TaskForm for creating new tasks

# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})  # Render the template with tasks

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form =TaskForm()
        return render(request, 'todoapp/add_task.html', {'form': form})  # Render the form for adding a new task
