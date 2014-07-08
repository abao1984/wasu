from django.conf.urls import patterns, include, url
from views import test_view, search_view

urlpatterns = patterns(
    '',
    (r'^test/$',test_view),
    (r'^search/$',search_view),
    
    )
