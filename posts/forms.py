from django import forms
from django.forms import ModelForm
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body']
        labels = {
          'body': 'Captions',
        }
        widgets = {
          'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption ...', 'class': 'font1 text-4xl'}),
          'url': forms.TextInput(attrs={'placeholder': 'Add url ...'}),
        }