from django.conf.urls import patterns, include, url
from views import machine_room_list_view,machine_room_view,machine_room_add_view 

urlpatterns = patterns(
    '',
    (r'^machine_room_list/$',machine_room_list_view),
    (r'^machine_room_add/$',machine_room_add_view),
    (r'^machine_room/$',machine_room_view),
    
    )
