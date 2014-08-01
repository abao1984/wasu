from django.conf.urls import patterns, include, url
from views import * 

urlpatterns = patterns(
    '',
    (r'^machine_room_list/$',machine_room_list_view),
    (r'^machine_room_add/$',machine_room_add_view),
    (r'^machine_room_detail/(?P<id>[0-9]+)/$',machine_room_detail_view),
    (r'^machine_room_advance_search/$',machine_room_advance_search_view),

    (r'^ups_add/(?P<room_id>[0-9]+)/$',ups_add_view),
    (r'^ups_detail/(?P<room_id>[0-9]+)/(?P<ups_id>[0-9]+)/$',ups_detail_view),
    (r'^ups_list/(?P<room_id>[0-9]+)/$',ups_list_view),
    
    (r'^battery_add/(?P<room_id>[0-9]+)/$',battery_add_view),
    (r'^battery_detail/(?P<room_id>[0-9]+)/(?P<battery_id>[0-9]+)/$',battery_detail_view),
    (r'^battery_list/(?P<room_id>[0-9]+)/$',battery_list_view),

    (r'^ac_add/(?P<room_id>[0-9]+)/$',ac_add_view),
    (r'^ac_detail/(?P<room_id>[0-9]+)/(?P<ac_id>[0-9]+)/$',ac_detail_view),
    (r'^ac_list/(?P<room_id>[0-9]+)/$',ac_list_view),

    (r'^switch_gear_add/(?P<room_id>[0-9]+)/$',switch_gear_add_view),
    (r'^column_head_add/(?P<room_id>[0-9]+)/$',column_head_add_view),
    (r'^distribution_add/(?P<room_id>[0-9]+)/$',distribution_add_view),
    (r'^switch_gear_detail/(?P<room_id>[0-9]+)/(?P<cabinet_id>[0-9]+)/$',switch_gear_detail_view),
    (r'^column_head_detail/(?P<room_id>[0-9]+)/(?P<cabinet_id>[0-9]+)/$',column_head_detail_view),
    (r'^distribution_detail/(?P<room_id>[0-9]+)/(?P<cabinet_id>[0-9]+)/$',distribution_detail_view),
    (r'^power_cabinet_list/(?P<room_id>[0-9]+)/$',power_cabinet_list_view),

    (r'^airswitch_add/(?P<room_id>[0-9]+)/(?P<cabinet_id>[0-9]+)/$', airswitch_add_view),
    (r'^airswitch_detail/(?P<room_id>[0-9]+)/(?P<cabinet_id>[0-9]+)/(?P<airswitch_id>[0-9]+)/$', airswitch_detail_view),

    (r'^monitor_list/(?P<room_id>[0-9]+)/$', monitor_list_view),
    (r'^monitor_add/(?P<room_id>[0-9]+)/$',monitor_add_view),
    (r'^monitor_detail/(?P<room_id>[0-9]+)/(?P<monitor_id>[0-9]+)/$',monitor_detail_view),
    
    (r'^entrance_guard_list/(?P<room_id>[0-9]+)/$', entrance_guard_list_view),
    (r'^entrance_guard_add/(?P<room_id>[0-9]+)/$',entrance_guard_add_view),
    (r'^entrance_guard_detail/(?P<room_id>[0-9]+)/(?P<entrance_guard_id>[0-9]+)/$',entrance_guard_detail_view),

    (r'^fire_fight_list/(?P<room_id>[0-9]+)/$', fire_fight_list_view),
    (r'^fire_fight_add/(?P<room_id>[0-9]+)/$',fire_fight_add_view),
    (r'^fire_fight_detail/(?P<room_id>[0-9]+)/(?P<fire_fight_id>[0-9]+)/$',fire_fight_detail_view),

#    (r'^machine_room_search/$',machine_room_search_view),
    (r'^ip_add/$',ip_add_view),

    )
