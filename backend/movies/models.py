from django.db import models
from ott.models import OTT
from django.db.models import Avg

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    thumbnail_url = models.URLField(blank=True, null=True)
    ott_services = models.ManyToManyField(OTT, related_name='movies')
    average_rating = models.FloatField(default=0.0)

    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    def __str__(self):
        return self.title