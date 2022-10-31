from django.forms import ModelForm
from django import forms
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
