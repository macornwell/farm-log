from django.conf import settings

"""
    Weather Settings
WEATHER_DATA = {'DJANGO_USERNAME':{
'wunder_key':'WUNDERGROUND_KEY',
'url':'URL_TO_USE',
}}


"""

default_data = {}
WEATHER_DATA = getattr(settings, 'WEATHER_DATA', default_data)

