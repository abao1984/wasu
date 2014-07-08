from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wasu.views.home', name='home'),
    url(r'^boss/', include('boss.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
