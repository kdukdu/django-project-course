from django.shortcuts import render

from forecast.forms import CityForm
from forecast.models import City
from forecast.utils import get_weather_info


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CityForm()

    cities = City.objects.order_by('-pk')[:5]
    all_cities_info = []

    for city in cities:
        city_info = get_weather_info(city)
        all_cities_info.append(city_info)

    context = {
        'all_cities_info': all_cities_info,
        'form': form
    }

    return render(request, 'forecast/index.html', context=context)
