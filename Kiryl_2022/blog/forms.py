from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
        labels = {
            'body': 'Comment',
            'author': 'Name'
        }
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', "cols": "40", "rows": "4"})
        }
