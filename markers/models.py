# from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class Marker(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name
from django.db import models


class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    
    

import django.contrib.gis.db.models as gis_models
from django.db import models


class Search(models.Model):
    term = models.CharField(max_length=255, null=True, blank=True)
    position = gis_models.PointField(srid=4326, dim=2)
    results_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.term, self.position)