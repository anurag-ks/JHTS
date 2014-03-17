from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=64)
    url = models.SlugField(max_length=16, unique=True)
    content = RichTextField()
    show_in_navbar = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
