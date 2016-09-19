from django.conf.urls import url
from core.views import add_feedback, model_details

urlpatterns = [
    url('^add/core/feedback', name='add_feedback', view=add_feedback),
    url('^details/(?P<model>[a-zA-Z]+)/(?P<id>\d+)', name='model_details', view=model_details),
]