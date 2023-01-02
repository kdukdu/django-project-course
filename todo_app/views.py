from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from .models import Task


class TasksList(ListView):
    model = Task
    template_name = 'todo_app/index.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.order_by('-created')


def task_create(request):
    title = request.POST.get('title')
    Task.objects.create(title=title)

    return redirect("todo:index")


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    is_completed = request.POST.get('is_completed', False)
    task.is_completed = bool(is_completed)
    task.save()
    return redirect("todo:index")


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("todo:index")
