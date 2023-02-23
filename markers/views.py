from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from account.models import User

from django.conf import settings
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from yelpapi import YelpAPI
from account.creator import createMarkers
from . import models as map_models
from . import serializers as map_serializers
from django.utils.decorators import method_decorator


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = map_serializers.SearchSerializer
    queryset = map_models.Search.objects.all()


class YelpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        yelp_api = YelpAPI(settings.YELP_API_KEY)

        search_results = yelp_api.search_query(**self.request.GET)

        term = request.GET.get('term')
        longitude = float(request.GET.get('longitude'))
        latitude = float(request.GET.get('latitude'))
        results_count = search_results['total']
        map_models.Search.objects.create(term=term,
                                         position=Point(longitude, latitude),
                                         results_count=results_count)

        return JsonResponse(search_results)

from .location import get_location


# @login_required(login_url='/accounts/login/')


class MarkersMapView(TemplateView):
    template_name = "map.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarkersMapView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        user=self.request.user
        user_details=get_location()
        user_details['user']=user
        print(user_details)
        createMarkers(user_details)
        context = super(MarkersMapView, self).get_context_data(*args, **kwargs)
        context['data'] = {"lng":user_details.get("latitude"),"lat":user_details.get("longitude"),"access_token":settings.GOOGLE_MAPS_API_KEY}
        return context

    #    "lat": response.get("latitude"),

