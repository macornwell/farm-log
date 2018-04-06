from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from core.views import get_add_model_form
from rest_framework.generics import ListAPIView
from observations.models import WeatherReading, Observation
from observations.forms import WeatherReadingForm, ObservationForm
from observations.serializers import WeatherReadingSerializer

ADD_OBSERVATION_TEMPLATE = 'observations/add_observation_model.html'


def add_weather_reading(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, WeatherReading, 'Weather Reading', 'datetime', WeatherReadingForm)


def add_observation(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, Observation, 'Observation', 'observation_date', ObservationForm)

from django.db import models as django_models
import django_filters
from rest_framework import filters
from rest_framework import viewsets

class WeatherReadingFilter(filters.FilterSet):
    class Meta:
        model = WeatherReading
        fields = {
            'datetime': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }


class WeatherReadingListView(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherReading.objects.all()
    serializer_class = WeatherReadingSerializer
    filter_class = WeatherReadingFilter
    filter_fields = {
        'datetime': ['gte', 'lte'],
    }

