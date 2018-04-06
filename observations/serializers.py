from rest_framework import serializers
from observations.models import WeatherReading


class WeatherReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherReading
        fields = ('weather_reading_id', 'datetime', 'state', 'temperature', 'unit')


