from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-on_create')
    context = {
        'title': 'Main page',
        'tasks': tasks
    }
    return render(request, 'todolist/index.html', context=context)


def about_us(request):
    return render(request, 'todolist/about_us.html')


def add_task(request):
    form = TaskForm
    context = {
        'title': 'Add new task',
        'form': form
    }
    return render(request, 'todolist/add_task.html', context=context)
