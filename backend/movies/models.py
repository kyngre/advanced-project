from django.db import models
from ott.models import OTT

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    thumbnail_url = models.URLField(blank=True, null=True)
    ott_services = models.ManyToManyField(OTT, related_name='movies')

    def __str__(self):
        return self.title