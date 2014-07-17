from django.contrib import admin
from django.forms import ModelForm
from models import *
from django.forms import TextInput, DateInput, Select, Textarea, CheckboxInput

class UPSForm(ModelForm):
    class Meta:
        model = UPS
        widgets = {
                 'start_date':DateInput(attrs={'class':'form-control'}),
                 'manufacturer':TextInput(attrs={'class':'form-control'}),
                 'specification':TextInput(attrs={'class':'form-control'}),
                 'code':TextInput(attrs={'class':'form-control'}),
                 'name':TextInput(attrs={'class':'form-control'}),
                 'asset_id':TextInput(attrs={'class':'form-control'}),
                 'equipment_life':TextInput(attrs={'class':'form-control'}),
                 'phone':TextInput(attrs={'class':'form-control'}),
                 'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                 'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                 'is_monitoring':Select(attrs={'class':'form-control'}),
                 'machine_room':Select(attrs={'class':'form-control'}),
                 'install_date':DateInput(attrs={'class':'form-control'}),

                 'gateway':TextInput(attrs={'class':'form-control'}),
                 'netcard_sn':TextInput(attrs={'class':'form-control'}),
                 'configuration':TextInput(attrs={'class':'form-control'}),
                }

class MachineRoomForm(ModelForm):
    class Meta:
        model= MachineRoom
        widgets = {
                'room_id':TextInput(attrs={'class':'form-control'}),
                'room_type':Select(attrs={'class':'form-control'}),
                'area':Select(attrs={'class':'form-control'}),
                'name':TextInput(attrs={'class':'form-control'}),
                'address':TextInput(attrs={'class':'form-control'}),
                'cover_range':Textarea(attrs={'class':'form-control','rows':'3'}),
#                'is_all_net':CheckboxInput(attrs={'class':'form-control'}),
'remark':Textarea(attrs={'class':'form-control', 'rows':'3'}),
                'phone':TextInput(attrs={'class':'form-control'}),
                'room_status':Select(attrs={'class':'form-control'}),
                'start_date':DateInput(attrs={'class':'form-control'}),
                }

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

