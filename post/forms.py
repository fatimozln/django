from django import forms
from . import models


class Create_post(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'body']
