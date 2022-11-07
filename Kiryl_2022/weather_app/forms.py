from django import forms
from django.core.exceptions import ValidationError

from weather_app.models import City
from weather_app.utils import get_weather


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not get_weather(name):
            raise ValidationError(f"I can't find city '{name}'")
        return name
