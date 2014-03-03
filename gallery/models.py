from django.db import models

class Gallery(models.Model):
	image = model.ImageField(upload_to = 'pic_folder/')
	description = model.CharField(max_length=50)

	def __unicode__(self):
        return self.description
