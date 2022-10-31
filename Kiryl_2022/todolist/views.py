from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .forms import TaskForm, TagForm
from .models import Task, Tag


# Create your views here.


class TodoIndex(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TodoIndex, self).get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Task.objects.order_by('-on_create')


# def tags_list(request):
#     tags = Tag.objects.all()
#
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('index')
#     else:
#         form = TagForm()
#
#     context = {
#         'title': 'Tags list',
#         'form': form,
#         'tags': tags
#     }
#     return render(request, 'todolist/tags_list.html', context=context)


class TagsList(CreateView):
    form_class = TagForm
    template_name = 'todolist/tags_list.html'
    model = Tag
    context_object_name = 'tags'
    success_url = reverse_lazy('tags_list')

    def get_context_data(self, **kwargs):
        context = super(TagsList, self).get_context_data(**kwargs)
        tags = Tag.objects.order_by('-pk')
        context['tags'] = tags
        return context



# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = TaskForm()
#
#     context = {
#         'title': 'Add new task',
#         'form': form
#     }
#     return render(request, 'todolist/add_task.html', context=context)


class AddTask(CreateView):
    form_class = TaskForm
    template_name = 'todolist/add_task.html'
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todolist/task_confirm_delete.html'
    success_url = reverse_lazy("index")


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags_list')
