from django import forms
from django.core.exceptions import ValidationError

from forecast.models import City
from forecast.utils import get_weather_info


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if get_weather_info(name) == None:
            raise ValidationError(f"I can't find city '{name}'")
        return name
