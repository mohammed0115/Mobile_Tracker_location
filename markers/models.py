from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from account.models import User

"""
{
    "ip": "102.121.219.69",
    "network": "102.121.219.0/24",
    "version": "IPv4",
    "city": "Khartoum",
    "region": "Khartoum",
    "region_code": "KH",
    "country": "SD",
    "country_name": "Sudan",
    "country_code": "SD",
    "country_code_iso3": "SDN",
    "country_capital": "Khartoum",
    "country_tld": ".sd",
    "continent_code": "AF",
    "in_eu": false,
    "postal": null,
    "latitude": 15.582,
    "longitude": 32.537,
    "timezone": "Africa/Khartoum",
    "utc_offset": "+0200",
    "country_calling_code": "+249",
    "currency": "SDG",
    "currency_name": "Pound",
    "languages": "ar-SD,en,fia",
    "country_area": 1861484.0,
    "country_population": 41801533,
    "asn": "AS36972",
    "org": "MTN"
}

"""
class Marker(models.Model):
    ip = models.CharField(max_length=15)
    network=models.CharField(max_length=15)
    version=models.CharField(max_length=15)
    city =models.CharField(max_length=70)
    region =models.CharField(max_length=70)
    region_code =models.CharField(max_length=7)
    country =models.CharField(max_length=7)
    country_name =models.CharField(max_length=70)
    country_code =models.CharField(max_length=7)
    country_code_iso3 =models.CharField(max_length=7)
    country_capital =models.CharField(max_length=70)
    country_tld =models.CharField(max_length=7)
    continent_code  = models.CharField(max_length=4)
    in_eu  = models.BooleanField()
    postal  = models.CharField(max_length=100)
    timezone  = models.CharField(max_length=70)
    utc_offset  = models.CharField(max_length=10)
    country_calling_code  = models.CharField(max_length=7)
    currency  = models.CharField(max_length=10)
    currency_name  = models.CharField(max_length=40)
    languages  = models.CharField(max_length=100)
    country_area  = models.CharField(max_length=40)
    asn  = models.CharField(max_length=20)
    org = models.CharField(max_length=20)
    country_population  = models.CharField(max_length=40)
    latitude  = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    location = models.PointField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ip
    
    # def save(self, *args, **kwargs):
    #     self.location.y = self.Latitude 
    #     self.mpoint.x   = self.Longitude    
    #     super(Marker, self).save(*args, **kwargs)  




class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50);
    IMEMI         = models.CharField(max_length=50)


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