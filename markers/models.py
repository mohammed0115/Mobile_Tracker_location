# from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from account.models import User
# from django.db import models
from django_google_maps import fields as map_fields
import django.contrib.gis.db.models as gis_models
from django.db import models

from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Point
class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

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
    ip = models.CharField(max_length=15,null=True)
    network=models.CharField(max_length=50,null=True)
    version=models.CharField(max_length=15,null=True)
    city =models.CharField(max_length=70,null=True)
    region =models.CharField(max_length=70,null=True)
    region_code =models.CharField(max_length=7,null=True)
    country =models.CharField(max_length=7,null=True)
    country_name =models.CharField(max_length=70,null=True)
    country_code =models.CharField(max_length=7,null=True)
    country_code_iso3 =models.CharField(max_length=7,null=True)
    country_capital =models.CharField(max_length=70,null=True)
    country_tld =models.CharField(max_length=7,null=True)
    continent_code  = models.CharField(max_length=4,null=True)
    in_eu  = models.BooleanField()
    postal  = models.CharField(max_length=100,null=True)
    timezone  = models.CharField(max_length=70,null=True)
    utc_offset  = models.CharField(max_length=10,null=True)
    country_calling_code  = models.CharField(max_length=7,null=True)
    currency  = models.CharField(max_length=10,null=True)
    currency_name  = models.CharField(max_length=40,null=True)
    languages  = models.CharField(max_length=100,null=True)
    country_area  = models.CharField(max_length=40,null=True)
    asn  = models.CharField(max_length=20,null=True)
    org = models.CharField(max_length=20,null=True)
    country_population  = models.CharField(max_length=40,null=True)
    latitude  = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    location = gis_models.PointField(geography=True, default=Point(0.0, 0.0))
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # address = map_fields.AddressField(max_length=200)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    def __str__(self):
        return self.ip
    
    # def save(self, *args, **kwargs):
    #     self.geolocation = f"{self.Latitude},{self.Longitude}"
    #     # self.mpoint.x   =    
    #     super(Marker, self).save(*args, **kwargs)  




class Phone(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50);
    IMEMI         = models.CharField(max_length=50)


class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)
    
    




class Search(models.Model):
    term = models.CharField(max_length=255, null=True, blank=True)
    position = gis_models.PointField(srid=4326, dim=2)
    results_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.term, self.position)