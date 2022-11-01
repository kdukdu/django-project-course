from django.urls import path

from .views import *

urlpatterns = [
    path('', TodoIndex.as_view(), name='index'),
    path('add/', AddTask.as_view(), name='add_task'),
    path('task/delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
    path('task/edit/<int:pk>', TaskEdit.as_view(), name='task_edit'),
    path('add_tag/', TagsList.as_view(), name='tags_list'),
    path('tag/delete/<int:pk>', TagDelete.as_view(), name='tag_delete'),

]
