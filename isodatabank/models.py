from django.db import models


class Data(models.Model):
    site_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
