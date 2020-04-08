#  Copyright (c) Code Written and Tested by Ahmed Emad in 08/04/2020, 22:20.

from django.db import models


class LocationModel(models.Model):
    """Model for every country"""

    country = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=5)
    confirmed = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('-confirmed',)

    @property
    def active(self):
        """calculates active cases"""
        return self.confirmed - (self.recovered + self.deaths)

