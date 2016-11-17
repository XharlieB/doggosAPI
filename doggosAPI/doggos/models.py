from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Size(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Raze(models.Model):
	nameRaze = models.CharField(max_length=120)
	size = models.ForeignKey(Size , related_name='size')
	def __str__(self):
		return self.nameRaze

class Doggo(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField(blank=False)
	image = models.ImageField(upload_to='doggosImages', blank=False)
	raze = models.ForeignKey(Raze, related_name='raze')
	user = models.ForeignKey(User, related_name='user')
	def __str__(self):
		return self.name


