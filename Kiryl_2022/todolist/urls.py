from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_task/', add_task, name='add_task'),
    path('about/', about_us, name='about_us'),
]