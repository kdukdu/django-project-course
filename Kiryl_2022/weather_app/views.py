from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from weather_app.forms import CityForm
from weather_app.models import City, CityList
from weather_app.utils import get_weather


# Create your views here.


class MainPage(CreateView):
    form_class = CityForm
    template_name = 'weather_app/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['cities'] = City.objects.order_by('-pk')
        try:
            context['delete'] = CityList.objects.all()[0]
        except:
            context['delete'] = None

        try:
            context['weather'] = get_weather(CityList.objects.order_by('-pk')[0].name)
        except:
            context['weather'] = get_weather()

        # context['list_cities'] = City.objects.values('name').distinct()
        return context

    def form_valid(self, form):
        CityList.objects.create(name=self.request.POST['name'])
        info = get_weather(form.cleaned_data['name'])
        form.instance.temperature = info['temperature']['actual']
        form.instance.icon = info['icon']
        form.instance.time = info['time']
        form.instance.res = info['time']
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


class GetUserLocationWeather(DeleteView):
    model = CityList

    def get_success_url(self):
        CityList.objects.all().delete()
        return reverse_lazy('index')
