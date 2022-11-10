from django.urls import path

from .views import *


app_name = 'weather'

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('requests/', RequestsList.as_view(), name='requests-list'),
    path('requests/<int:pk>/delete/', RequestDelete.as_view(), name='request-delete'),
    path('delete/<int:pk>/', GetUserLocationWeather.as_view(), name='get-user-location-weather'),
]
