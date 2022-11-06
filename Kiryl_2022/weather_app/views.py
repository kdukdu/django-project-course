from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from weather_app.forms import CityForm
from weather_app.models import City
from weather_app.utils import get_weather_info, get_weather_by_user_location


# Create your views here.


class MainPage(CreateView):
    form_class = CityForm
    template_name = 'weather_app/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['cities'] = City.objects.order_by('-pk')
        context['user_location_weather'] = get_weather_by_user_location()
        return context

    def form_valid(self, form):
        info = get_weather_info(form.cleaned_data['name'])
        form.instance.temperature = info['temperature']
        form.instance.icon = info['icon']
        form.instance.time = info['time']
        form.save()
        return super().form_valid(form)


class RequestsList(ListView):
    model = City
    paginate_by = 4
    template_name = 'weather_app/requests.html'
    context_object_name = 'cities'


class RequestDelete(DeleteView):
    model = City

    def get_success_url(self):
        if self.request.POST.get('requests-delete-from-list'):
            return reverse_lazy('requests')
        else:
            return reverse_lazy('index')
