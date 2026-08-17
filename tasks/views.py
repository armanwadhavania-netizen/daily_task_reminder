from django.shortcuts import render, redirect
from .models import Task, Reminder
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('due_date', 'due_time')
    reminders = Reminder.objects.all().order_by('-created_at')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'reminders': reminders,
    })


def add_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {
        'form': form
    })