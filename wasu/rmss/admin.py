from django.contrib import admin
from django.forms import ModelForm
from models import *

class MachineRoomForm(ModelForm):
    class Meta:
        model= MachineRoom

# Register your models here.
admin.site.register(MachineRoomType)
admin.site.register(MachineRoomUsage)
admin.site.register(Area)
admin.site.register(MachineRoom)
admin.site.register(Equipment)
admin.site.register(UPS)
admin.site.register(Battery)
admin.site.register(AirSwitch)
admin.site.register(SwitchGearCabinet)
admin.site.register(ColumnHeadCabinet)
admin.site.register(DistributionCabinet)
admin.site.register(MonitorEquipment)
admin.site.register(EntranceGuardEquipment)
admin.site.register(FirefightingEquipment)

