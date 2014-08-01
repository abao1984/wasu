from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from rmss.models import *
from tastypie import fields, utils

class MachineRoomTypeResource(ModelResource):
    class Meta:
        queryset = MachineRoomType.objects.all()
        allowed_methods = ['get']
        resource_name = 'room_type'
#        filtering = {
#                    'name':ALL
#                }

class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        allowed_methods = ['get']
        resource_name = 'area'
#        filtering = {
#                    'name':ALL
#                }


class MachineRoomResource(ModelResource):
    room_type = fields.ForeignKey(MachineRoomTypeResource, 'room_type', null=True,blank=True, full=True)
    area = fields.ForeignKey(AreaResource, 'area', null=True, blank=True, full=True)

    class Meta:
        queryset = MachineRoom.objects.all()
        allowed_methods = ['get']
        resource_name = 'machine_room'
        filtering = {
                    'name':ALL,
                    'room_id':ALL,
                    'room_type':ALL_WITH_RELATIONS,
                    'area':ALL_WITH_RELATIONS,
                    'address':ALL,
                    'is_all_net':ALL,
                    'phone':ALL,
                    'room_status':ALL,
                    'start_date':ALL,
                }
