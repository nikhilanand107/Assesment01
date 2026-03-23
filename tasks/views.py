from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils.dateparse import parse_date

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/dashboard.html", {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority', 'Medium')
        
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            due_date=parse_date(due_date) if due_date else None,
            priority=priority,
            status='Pending'
        )
        return redirect('dashboard')
        
    return render(request, "tasks/add_tasks.html")

@login_required
def categories(request):
    return render(request, "tasks/category.html")

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, "tasks/task_detail.html", {'task': task})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.category = request.POST.get('category', task.category)
        due_date = request.POST.get('due_date')
        if due_date:
            task.due_date = parse_date(due_date)
        task.priority = request.POST.get('priority', task.priority)
        task.status = request.POST.get('status', task.status)
        task.save()
        return redirect('dashboard')
        
    return render(request, "tasks/task_form.html", {'task': task, 'title': 'Edit Task'})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "tasks/register.html", {"form": form})
