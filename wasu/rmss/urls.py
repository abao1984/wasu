from django.conf.urls import patterns, include, url
from views import machine_room_list_view,machine_room_detail_view,machine_room_add_view,machine_room_advance_search_view,ups_add_view, ups_list_view 

urlpatterns = patterns(
    '',
    (r'^machine_room_list/$',machine_room_list_view),
    (r'^machine_room_add/$',machine_room_add_view),
    (r'^machine_room_detail/(?P<id>[0-9]+)/$',machine_room_detail_view),
    (r'^machine_room_advance_search/$',machine_room_advance_search_view),

    (r'^ups_add/(?P<room_id>[0-9]+)/$',ups_add_view),
    (r'^ups_list/(?P<room_id>[0-9]+)/$',ups_list_view),
    
    )
