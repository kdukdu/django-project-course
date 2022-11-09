from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('requests/', RequestsList.as_view(), name='requests'),
    path('requests/<int:pk>/delete/', RequestDelete.as_view(), name='request_delete'),
    path('delete/<int:pk>/', GetUserLocationWeather.as_view(), name='get_user_location_weather'),
]
