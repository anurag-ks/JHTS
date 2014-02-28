from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

	def __unicode__(self):
		return self.title
	


