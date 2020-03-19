from django.db import models


class LocationModel(models.Model):
    """Model for every country"""

    country = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=5, unique=True)
    confirmed = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('-confirmed',)
