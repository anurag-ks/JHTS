from django.db import models

class Gallery(models.Model):
	image = models.ImageField(upload_to = 'pic_folder/')
	description = models.CharField(max_length=50)

	def __unicode__(self):
		return self.description
