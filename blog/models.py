from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post_id = models.ForeignKey(Blog)
    author = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content
