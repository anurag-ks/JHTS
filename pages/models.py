from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=16)
    content = RichTextField()

    def __unicode__(self):
        return self.title
