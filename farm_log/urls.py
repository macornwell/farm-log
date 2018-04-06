from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import login
from farm_log import settings
from farm_log.views import home, home_with_page, worksite
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
import core.urls as CoreUrls
import observations.urls as ObservationUrls
import work.urls as WorkUrls
import livestock.urls as LivestockUrls
import plants.urls as PlantsUrls


router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^(?P<page>-?\d+)/$', home_with_page, name='home'),
    #url(r'^(?P<page>.+)/$', home, name='home'),
    #url(r'^work-site/$', worksite, name='work-site'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', login, {'template_name': 'admin/login.html'})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += CoreUrls.urlpatterns
urlpatterns += ObservationUrls.urlpatterns
urlpatterns += WorkUrls.urlpatterns
urlpatterns += LivestockUrls.urlpatterns
urlpatterns += PlantsUrls.urlpatterns

###################
# Rest Framework
###################

urlpatterns += [
    url(r'^api/', include(router.urls), name='api'),
    #url(r'^api/log_message', post_log_messages_json, name='log_message'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth/token/$', obtain_jwt_token),
    url(r'^api/v1/auth/token/verify/$', verify_jwt_token),
    url(r'^api/v1/auth/token/refresh/$', refresh_jwt_token),
]

