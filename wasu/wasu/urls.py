from django.conf.urls import patterns, include, url
from tastypie.api import Api
from rmss.api.resources import * 
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(MachineRoomResource())
v1_api.register(MachineRoomTypeResource())
v1_api.register(AreaResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wasu.views.home', name='home'),
    url(r'^boss/', include('boss.urls')),
    url(r'^rmss/', include('rmss.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
