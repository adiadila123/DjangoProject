from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True) # Add a unique slug for the channel



