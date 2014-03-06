from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from pages.models import Page


class PageForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
