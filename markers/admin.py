
from django.contrib.gis import admin as admin_gis

from markers.models import Marker

from django.contrib.gis import admin as gis_admin
from django.contrib import admin
from . import models as map_models
from django.conf import settings
from django.contrib import admin
from .models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )


admin.site.register(map_models.Search, gis_admin.GeoModelAdmin)


@admin.register(Marker)
class MarkerAdmin(admin_gis.GeoModelAdmin):
    list_display = ("name", "location")