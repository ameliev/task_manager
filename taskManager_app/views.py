from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tasks, User
from .forms import TaskForm


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def tasks_list(request, user_id):
    tasks = Tasks.objects.all().filter(user_id=user_id)
    user = get_object_or_404(User, id=user_id)
    return render(
        request, 'tasks/tasks_list.html', {'tasks': tasks, 'user': user}
    )


def show_task(request, id):
    task = get_object_or_404(Tasks, id=id)
    return render(request, 'tasks/show_task.html', {'task': task})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('tasksList', user_id=task.user_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'forms/editTask.html', {
        'form': form,
        'user_id': task.user_id
    })


@login_required
def remove_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect('tasksList', user_id=task.user_id)


def done_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.done = True
    task.save()
    return redirect('tasksList', user_id=task.user_id)


def new_task(request, user_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = user_id
            task.save()
            return redirect('tasksList', user_id=task.user_id)
    else:
        form = TaskForm()
    return render(request, 'forms/editTask.html', {
        'form': form,
        'user_id': user_id
    })
