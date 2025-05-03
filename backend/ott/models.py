from django.db import models

class OTT(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name