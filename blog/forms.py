from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget

from .models import Comment, Post, CustomUser


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment'
        }


class RegisterUserForm(UserCreationForm):
    attrs = {'class': 'form-control'}
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=attrs))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'profile_picture')


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'status', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "4"}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control'})
        }
