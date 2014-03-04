from gallery.models import Gallery
from django import forms
from django.forms import ModelForm



class GalleryForm(ModelForm):
    class Meta:
    	model = Gallery