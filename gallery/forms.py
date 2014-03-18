from gallery.models import GalleryPhoto
from django.forms import ModelForm


class GalleryForm(ModelForm):
    class Meta:
        model = GalleryPhoto
