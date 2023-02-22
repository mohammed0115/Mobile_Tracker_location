
from django.contrib.gis import admin as admin_gis

from markers.models import Marker

from django.contrib.gis import admin as gis_admin
from django.contrib import admin
from . import models as map_models
from django.conf import settings
from django.contrib import admin
from .models import Venue,Rental,Phone
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


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


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('user', 'serial_number', 'IMEMI',)

@admin.register(Marker)
class MarkerAdmin(admin_gis.GeoModelAdmin):
    list_display = ['ip', 'network', 'version', 'city', 'region', 'region_code', 
                    'country', 'country_name', 'country_code', 'country_code_iso3', 
                    'country_capital', 'country_tld', 'continent_code', 'in_eu',
                      'postal', 'latitude', 'longitude', 'timezone', 'utc_offset',
                        'country_calling_code',
                     'currency', 'currency_name', 'languages', 'country_area', 'country_population', 'asn', 'org','user']
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(user=request.user)
    # @admin.display(empty_value='???')
    # def view_user(self, obj):
    #     return obj.user


