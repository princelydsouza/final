from django.db import models

# Create your models here.

class User(models.Model):
	fname = models.CharField(max_length=10)
	lname = models.CharField(max_length=10)
	def __str__ (self):
		return self.name


class Todo(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	#
	created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	CHOICES= (

		('Created', 'Created'),
		('Inprocess', 'Inprocess'),
		('Done', 'Done'),
	
	)
	status = models.CharField(choices=CHOICES,max_length=100)