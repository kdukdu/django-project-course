from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'title': 'Main page',
        'tasks': tasks
    }
    return render(request, 'todolist/index.html', context=context)


def about_us(request):
    return render(request, 'todolist/about_us.html')
