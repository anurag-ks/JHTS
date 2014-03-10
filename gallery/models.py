from django.db import models
from django_resized import ResizedImageField

class GalleryPhoto(models.Model):
    image = ResizedImageField(max_width=500, max_height=300, upload_to='pic_folder/')
    description = models.TextField()

    def __unicode__(self):
        return self.image.url
