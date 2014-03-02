from main.models import Blog
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget


class BlogForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
