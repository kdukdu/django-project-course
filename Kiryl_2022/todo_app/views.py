from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import TaskForm, TagForm
from .models import Task, Tag


# Create your views here.


class MainPage(ListView):
    model = Task
    template_name = 'todo_app/index.html'
    context_object_name = 'tasks'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Task.objects.order_by('-on_create')


class TagsList(CreateView):
    form_class = TagForm
    template_name = 'todo_app/tags_list.html'
    model = Tag
    context_object_name = 'tags'
    success_url = reverse_lazy('tags_list')

    def get_context_data(self, **kwargs):
        context = super(TagsList, self).get_context_data(**kwargs)
        tags = Tag.objects.order_by('-pk')
        context['tags'] = tags
        return context


class AddTask(CreateView):
    form_class = TaskForm
    template_name = 'todo_app/add_task.html'
    success_url = reverse_lazy('index_todo')


class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'todo_app/edit_task.html'

    def get_form(self, *args, **kwargs):
        form = super(TaskEdit, self).get_form(*args, **kwargs)
        form.fields["title"].widget.attrs["class"] = "form-control"
        form.fields["description"].widget.attrs["class"] = "form-control"
        form.fields["deadline"].widget.attrs["class"] = "form-control"
        form.fields["tags"].widget.attrs["class"] = "select"
        return form


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo_app/task_confirm_delete.html'
    success_url = reverse_lazy("index_todo")


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags_list')


class TasksFilterByTag(ListView):
    model = Task
    template_name = 'todo_app/tasks_filter_by_tag.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(tags__name=self.kwargs['tag_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TasksFilterByTag, self).get_context_data(**kwargs)
        context['tag_slug'] = self.kwargs['tag_slug']
        return context
