from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=255)
    tags = TaggableManager()