import json
import urllib.request
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from observations.settings import WEATHER_DATA
from observations.models import WeatherReading

URL_FORMAT = 'http://api.wunderground.com/api/{0}/conditions/q/{1}/{2}.json'


WUNDERWEATHER_TO_WEATHER_STATE = {
    'Overcast': 'o',
    'Clear': 's',
    'Partly Cloudy': 'p',
    'Scattered Clouds': 'p',
    'Cloudy': 'c',
    }


class Command(BaseCommand):
    help = "Pulls weather information from Wunderground and logs it."

    def handle(self, *args, **options):
        self.stdout.write('Pulling weather')
        for username in WEATHER_DATA:
            if not username:
                raise Exception('No username provided')
            user = User.objects.filter(username=username).first()
            if not user:
                raise Exception('Username {0} not found'.format(username))
            data = WEATHER_DATA[username]
            state = data['state']
            if not state:
                raise Exception('No State provided')
            city = data['city']
            if not city:
                raise Exception('No city provided')
            key = data['wunder_key']
            if not key:
                raise Exception('No key provided')
            url = URL_FORMAT.format(key, state, city)
            response = urllib.request.urlopen(url)
            stringResponse = response.readall().decode('utf-8')
            obj = json.loads(stringResponse)
            current = obj['current_observation']
            currentWeather = current['weather']
            temp = current['temp_f']
            weatherState = self.get_weather_state_for_wunderground_weather(currentWeather)
            reading = WeatherReading()
            reading.state = weatherState
            reading.temperature = temp
            reading.user = user
            reading.save()

    def get_weather_state_for_wunderground_weather(self, weather):
        state = 's'
        if weather in WUNDERWEATHER_TO_WEATHER_STATE:
            state = WUNDERWEATHER_TO_WEATHER_STATE[weather]
        else:
            if 'Rain' in weather or 'Drizzle' in weather:
                state = 'r'
            elif 'Snow' in weather or 'Ice' in weather or 'Hail' in weather:
                state = 'n'
        return state



