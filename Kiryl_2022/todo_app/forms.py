from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Task, Tag


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "deadline", "tags")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'select'})
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Tag.objects.filter(name=name):
            raise ValidationError(f"Tag '{name}' has already exists!")
        elif ' ' in name:
            raise ValidationError("Tag must not contain spaces")
        return name
