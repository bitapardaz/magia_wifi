# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model): 
	
	name = models.CharField(max_length=200)
	confirmed = models.BooleanField(default = False)
	thumbnail = models.ImageField(upload_to='images',null=True,max_length=300)
	date_published = models.DateTimeField(auto_now=True,editable=True)

	def __unicode__(self): 
		return self.name


class Movie(models.Model): 
	
	name = models.CharField(max_length=200)
#	file_location = models.FileField(upload_to='movies',null=True,max_length=300)
#	image = models.ImageField(upload_to='images',null=True,max_length=300)
	confirmed = models.BooleanField(default=False)
	price = models.IntegerField(default =0)
	category = models.ForeignKey(Category)
	date_published = models.DateTimeField(auto_now=True,editable=True)
	file_path = models.FilePathField(path="/mnt/FlashDrive/wifi_storage/movies/",allow_folders=False,null=True,blank=True)	


	def __unicode__(self): 
		return self.name



