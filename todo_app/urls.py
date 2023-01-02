from django.urls import path

from .views import *


app_name = 'todo'

urlpatterns = [
    path('', TasksList.as_view(), name='index'),
    path('task/add/', task_create, name='task_create'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/<int:pk>/update/', task_update, name='task_update'),
]
