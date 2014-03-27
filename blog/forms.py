from blog.models import Blog, Comment
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget


class BlogForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ("post_id",)
