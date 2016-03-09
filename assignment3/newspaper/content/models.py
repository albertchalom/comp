from __future__ import unicode_literals

from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
	text = models.TextField()

class Image(Content):
	path = models.CharField(max_length = 500) 


class Contributor(models.Model):
	first_name = models.CharField(max_length = 32)
	last_name = models.CharField(max_length = 32)
	content = Content.objects.all()
	def die(self): 
		self.delete()
# Create your models here.
