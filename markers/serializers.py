from rest_framework_gis import serializers

from markers.models import Marker
from rest_framework_gis import serializers

from . import models as map_models


class SearchSerializer(serializers.GeoModelSerializer):

    class Meta:
        model = map_models.Search
        exclude = []


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Marker