from django.urls import reverse_lazy
from django.views.generic import CreateView

from weather_app.forms import CityForm
from weather_app.models import City
from weather_app.utils import get_weather_info


# Create your views here.


class MainPage(CreateView):
    form_class = CityForm
    template_name = 'weather_app/index.html'
    success_url = reverse_lazy('index')
    context_object_name = 'cities'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['cities'] = City.objects.order_by('-pk')
        return context

    def form_valid(self, form):
        info = get_weather_info(form.cleaned_data['name'])
        form.instance.temperature = info['temperature']
        form.instance.icon = info['icon']
        form.instance.time = info['time']
        form.save()
        return super().form_valid(form)
