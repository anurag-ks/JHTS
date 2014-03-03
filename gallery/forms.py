from django import forms

class GalleryForm(forms.Form):
    image = forms.ImageField()
    description = forms.CharField(max_length=50)