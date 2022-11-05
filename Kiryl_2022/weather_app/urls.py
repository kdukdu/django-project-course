from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('requests/', RequestsList.as_view(), name='requests'),
    path('requests/delete/<int:pk>', RequestDelete.as_view(), name='request_delete'),
]
