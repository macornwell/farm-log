from django.conf.urls import url
from observations.views import add_weather_reading, add_observation
from observations import views

urlpatterns = [
    url('^add/observations/observation', name='add_observation', view=add_observation),
    url('^add/observations/weather', name='add_weather', view=add_weather_reading),
    url(r'^api/v1/weather/$', views.WeatherReadingListView.as_view({'get':'list'}), name='weather-readings-list'),
]
