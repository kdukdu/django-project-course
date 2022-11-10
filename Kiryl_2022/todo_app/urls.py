from django.urls import path

from .views import *


app_name = 'todo'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('tasks/filter/<slug:tag_slug>', TasksFilterByTag.as_view(), name='tag_filter'),
    path('task/add/', AddTask.as_view(), name='add_task'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('task/<int:pk>/edit/', TaskEdit.as_view(), name='task_edit'),
    path('tag/add/', TagsList.as_view(), name='tags_list'),
    path('tag/<int:pk>/delete/', TagDelete.as_view(), name='tag_delete'),

]
