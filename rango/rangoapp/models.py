from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(max_length=128, unique=False)
	views = models.IntegerField(default=0, unique=False)
	likes = models.IntegerField(default=0, unique=False)
	slug = models.SlugField(unique=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
	    return self.name


class Page(models.Model):
 	  category = models.ForeignKey(Category)
 	  title = models.CharField(max_length=128)
 	  url = models.URLField(max_length=128)
 	  views = models.IntegerField(default=0)
 	  def __str__(self):
 	  	return self.title


