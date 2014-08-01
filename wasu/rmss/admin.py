# coding=UTF-8
from django.contrib import admin
from django.forms import ModelForm
from models import *
from django.forms import TextInput, DateInput, Select, Textarea, CheckboxInput,HiddenInput

class IPAddressForm(ModelForm):
    class Meta:
        model = IPAddress
        widgets = {
            'address':TextInput(attrs={'class':'form-control'}),
            'subnet_mask':TextInput(attrs={'class':'form-control'}),
            'machine_room':TextInput(attrs={'class':'form-control'}),
            'bussiness_type':Select(attrs={'class':'form-control'}),
            'status':Select(attrs={'class':'form-control'}),
            'record_user':HiddenInput(attrs={'class':'form-control'}),
            'record_date':HiddenInput(attrs={'class':'form-control'}),
            'change_user':HiddenInput(attrs={'class':'form-control'}),
            'change_date':HiddenInput(attrs={'class':'form-control'}),
            'max_host_count':HiddenInput(attrs={'class':'form-control'}),
            'parent':HiddenInput(attrs={'class':'form-control'}),
            'remark':Textarea(attrs={'class':'form-control','rows':'3'}),
                }
        labels = {
            'address':u'IP地址',
            'subnet_mask':u'子网掩码',
            'remark':u'备注',
            'bussiness_type':u'业务类型',
            'status':u'是否启用',
            'max_host_count':u'最大主机数',
            'parent':u'上级IP地址',
            'machine_room':u'所属机房',
                }

class FirefightingEquipmentForm(ModelForm):
    class Meta:
        model = FirefightingEquipment
        widgets = {
            'start_date':TextInput(attrs={'class':'form-control'}),
            'is_started':HiddenInput(attrs={'class':'form-control'}),
            'manufacturer':TextInput(attrs={'class':'form-control'}),
            'specification':TextInput(attrs={'class':'form-control'}),
            'code':TextInput(attrs={'class':'form-control'}),
            'status':Select(attrs={'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
            'install_date':TextInput(attrs={'class':'form-control'}),
            'asset_id':TextInput(attrs={'class':'form-control'}),
            'equipment_life':TextInput(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
            'maintenance_unit':TextInput(attrs={'class':'form-control'}),
            'is_monitoring':Select(attrs={'class':'form-control'}),
            'machine_room':HiddenInput(attrs={'class':'form-control'}),

                }
        labels = {
            'start_date':u'启动日期',
            'is_started':u'设备厂家',
            'manufacturer':u'设备厂家',
            'specification':u'规格型号',
            'code':u'消防编号',
            'name':u'消防名称',
            'install_date':u'安装日期',
            'asset_id':u'资产编号',
            'equipment_life':u'设备使用年限',
            'phone':u'厂家联系电话',
            'maintenance_cycles':u'维保周期',
            'maintenance_unit':u'代维单位',
            'is_monitoring':u'是否监控',
            'machine_room':u'机房',
            'status':u'消防状态'
        }


class EntranceGuardEquipmentForm(ModelForm):
    class Meta:
        model = MonitorEquipment
        widgets = {
            'start_date':TextInput(attrs={'class':'form-control'}),
            'is_started':HiddenInput(attrs={'class':'form-control'}),
            'manufacturer':TextInput(attrs={'class':'form-control'}),
            'specification':TextInput(attrs={'class':'form-control'}),
            'code':TextInput(attrs={'class':'form-control'}),
            'status':Select(attrs={'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
            'install_date':TextInput(attrs={'class':'form-control'}),
            'asset_id':TextInput(attrs={'class':'form-control'}),
            'equipment_life':TextInput(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
            'maintenance_unit':TextInput(attrs={'class':'form-control'}),
            'is_monitoring':Select(attrs={'class':'form-control'}),
            'machine_room':HiddenInput(attrs={'class':'form-control'}),

                }
        labels = {
            'start_date':u'启动日期',
            'is_started':u'设备厂家',
            'manufacturer':u'设备厂家',
            'specification':u'规格型号',
            'code':u'门禁编号',
            'name':u'门禁名称',
            'install_date':u'安装日期',
            'asset_id':u'资产编号',
            'equipment_life':u'设备使用年限',
            'phone':u'厂家联系电话',
            'maintenance_cycles':u'维保周期',
            'maintenance_unit':u'代维单位',
            'is_monitoring':u'是否监控',
            'machine_room':u'机房',
            'status':u'门禁状态'
        }


class MonitorEquipmentForm(ModelForm):
    class Meta:
        model = MonitorEquipment
        widgets = {
            'start_date':TextInput(attrs={'class':'form-control'}),
            'is_started':HiddenInput(attrs={'class':'form-control'}),
            'manufacturer':TextInput(attrs={'class':'form-control'}),
            'specification':TextInput(attrs={'class':'form-control'}),
            'code':TextInput(attrs={'class':'form-control'}),
            'status':Select(attrs={'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
            'install_date':TextInput(attrs={'class':'form-control'}),
            'asset_id':TextInput(attrs={'class':'form-control'}),
            'equipment_life':TextInput(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
            'maintenance_unit':TextInput(attrs={'class':'form-control'}),
            'is_monitoring':Select(attrs={'class':'form-control'}),
            'machine_room':HiddenInput(attrs={'class':'form-control'}),
        }
        labels = {
            'start_date':u'启动日期',
            'is_started':u'设备厂家',
            'manufacturer':u'设备厂家',
            'specification':u'规格型号',
            'code':u'监控编号',
            'name':u'监控名称',
            'install_date':u'安装日期',
            'asset_id':u'资产编号',
            'equipment_life':u'设备使用年限',
            'phone':u'厂家联系电话',
            'maintenance_cycles':u'维保周期',
            'maintenance_unit':u'代维单位',
            'is_monitoring':u'是否监控',
            'machine_room':u'机房',
            'status':u'监控状态'
        }

class AirSwitchForm(ModelForm):
    class Meta:
        model = AirSwitch
        widgets = {
            'name':TextInput(attrs={'class':'form-control'}),
            'configuration':Select(attrs={'class':'form-control'}),
            'total_count':TextInput(attrs={'class':'form-control'}),
            'used_count':TextInput(attrs={'class':'form-control'}),
            'switch_gear_cabinet':HiddenInput(attrs={'class':'form-control'}),
            'remark':Textarea(attrs={'class':'form-control','rows':'3'}),
            }
        labels = {
            'name':u'名称',
            'configuration':u'空开配置',
            'total_count':u'配置数量',
            'used_count':u'已用数量',
            'switch_gear_cabinet':u'电力柜',
            }

class SwitchGearCabinetForm(ModelForm):
    class Meta:
        model = SwitchGearCabinet
        widgets = {
                'name':TextInput(attrs={'class':'form-control'}),
                'start_date':TextInput(attrs={'class':'form-control'}),
                'is_started':HiddenInput(attrs={'class':'form-control'}),
                'manufacturer':TextInput(attrs={'class':'form-control'}),
                'specification':TextInput(attrs={'class':'form-control'}),
                'code':TextInput(attrs={'class':'form-control'}),
                'install_date':TextInput(attrs={'class':'form-control'}),
                'asset_id':TextInput(attrs={'class':'form-control'}),
                'equipment_life':TextInput(attrs={'class':'form-control'}),
                'phone':TextInput(attrs={'class':'form-control'}),
                'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                'is_monitoring':Select(attrs={'class':'form-control'}),
                'machine_room':HiddenInput(attrs={'class':'form-control'}),

                'power_supply':Select(attrs={'class':'form-control'}),
                'oil_machine_interface':Select(attrs={'class':'form-control'}),
                'lightning_protection':Select(attrs={'class':'form-control'}),
                'ammeter':Select(attrs={'class':'form-control'}),
                'ammeter_magnification':TextInput(attrs={'class':'form-control'}),
                }
        labels = {
                'name':u'名称',
                'start_date':u'启用日期',
                'is_started':u'是否启用',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'编号',
                'install_date':u'安装日期',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',
                'power_supply':u'供电方式',
                'oil_machine_interface':u'油机接口',
                'lightning_protection':u'防雷器',
                'ammeter':u'电表',
                'ammeter_magnification':u'电表倍率',
                }

class ColumnHeadCabinetForm(SwitchGearCabinetForm):
    class Meta:
        model = ColumnHeadCabinet
        widgets = {
                'name':TextInput(attrs={'class':'form-control'}),
                'start_date':TextInput(attrs={'class':'form-control'}),
                'is_started':HiddenInput(attrs={'class':'form-control'}),
                'manufacturer':TextInput(attrs={'class':'form-control'}),
                'specification':TextInput(attrs={'class':'form-control'}),
                'code':TextInput(attrs={'class':'form-control'}),
                'install_date':TextInput(attrs={'class':'form-control'}),
                'asset_id':TextInput(attrs={'class':'form-control'}),
                'equipment_life':TextInput(attrs={'class':'form-control'}),
                'phone':TextInput(attrs={'class':'form-control'}),
                'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                'is_monitoring':Select(attrs={'class':'form-control'}),
                'machine_room':HiddenInput(attrs={'class':'form-control'}),

                'power_supply':Select(attrs={'class':'form-control'}),
                'oil_machine_interface':Select(attrs={'class':'form-control'}),
                'lightning_protection':Select(attrs={'class':'form-control'}),
                'ammeter':Select(attrs={'class':'form-control'}),
                'ammeter_magnification':TextInput(attrs={'class':'form-control'}),
                }
        labels = {
                'name':u'名称',
                'start_date':u'启用日期',
                'is_started':u'是否启用',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'编号',
                'install_date':u'安装日期',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',
                'power_supply':u'供电方式',
                'oil_machine_interface':u'油机接口',
                'lightning_protection':u'防雷器',
                'ammeter':u'电表',
                'ammeter_magnification':u'电表倍率',
                }

class DistributionCabinetForm(SwitchGearCabinetForm):
    class Meta:
        model = DistributionCabinet
        widgets = {
                'name':TextInput(attrs={'class':'form-control'}),
                'start_date':TextInput(attrs={'class':'form-control'}),
                'is_started':HiddenInput(attrs={'class':'form-control'}),
                'manufacturer':TextInput(attrs={'class':'form-control'}),
                'specification':TextInput(attrs={'class':'form-control'}),
                'code':TextInput(attrs={'class':'form-control'}),
                'install_date':TextInput(attrs={'class':'form-control'}),
                'asset_id':TextInput(attrs={'class':'form-control'}),
                'equipment_life':TextInput(attrs={'class':'form-control'}),
                'phone':TextInput(attrs={'class':'form-control'}),
                'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                'is_monitoring':Select(attrs={'class':'form-control'}),
                'machine_room':HiddenInput(attrs={'class':'form-control'}),

                'power_supply':Select(attrs={'class':'form-control'}),
                'oil_machine_interface':Select(attrs={'class':'form-control'}),
                'lightning_protection':Select(attrs={'class':'form-control'}),
                'ammeter':Select(attrs={'class':'form-control'}),
                'ammeter_magnification':TextInput(attrs={'class':'form-control'}),
                }
        labels = {
                'name':u'名称',
                'start_date':u'启用日期',
                'is_started':u'是否启用',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'编号',
                'install_date':u'安装日期',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',
                'power_supply':u'供电方式',
                'oil_machine_interface':u'油机接口',
                'lightning_protection':u'防雷器',
                'ammeter':u'电表',
                'ammeter_magnification':u'电表倍率',
                }


class ACForm(ModelForm):
    class Meta:
        model = AirConditioning
        widgets = {
                'name':TextInput(attrs={'class':'form-control'}),
                'start_date':TextInput(attrs={'class':'form-control'}),
                'is_started':HiddenInput(attrs={'class':'form-control'}),
                'manufacturer':TextInput(attrs={'class':'form-control'}),
                'specification':TextInput(attrs={'class':'form-control'}),
                'code':TextInput(attrs={'class':'form-control'}),
                'install_date':TextInput(attrs={'class':'form-control'}),
                'asset_id':TextInput(attrs={'class':'form-control'}),
                'equipment_life':TextInput(attrs={'class':'form-control'}),
                'phone':TextInput(attrs={'class':'form-control'}),
                'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                'is_monitoring':Select(attrs={'class':'form-control'}),
                'machine_room':HiddenInput(attrs={'class':'form-control'}),
 
                }
        labels = {
                'name':u'名称',
                'start_date':u'启用日期',
                'is_started':u'是否启用',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'空调编号',
                'install_date':u'安装日期',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',

                }

class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        widgets = {
                 'name':TextInput(attrs={'class':'form-control'}),
                 'start_date':TextInput(attrs={'class':'form-control'}),
                 'is_started':HiddenInput(attrs={'class':'form-control'}),
                 'manufacturer':TextInput(attrs={'class':'form-control'}),
                 'specification':TextInput(attrs={'class':'form-control'}),
                 'code':HiddenInput(attrs={'class':'form-control'}),
                 'install_date':TextInput(attrs={'class':'form-control'}),
                 'asset_id':TextInput(attrs={'class':'form-control'}),
                 'equipment_life':TextInput(attrs={'class':'form-control'}),
                 'phone':TextInput(attrs={'class':'form-control'}),
                 'maintenance_cycles':TextInput(attrs={'class':'form-control'}),
                 'maintenance_unit':TextInput(attrs={'class':'form-control'}),
                 'is_monitoring':HiddenInput(attrs={'class':'form-control'}),
                 'machine_room':HiddenInput(attrs={'class':'form-control'}),

                 'battery_type':Select(attrs={'class':'form-control'}),
                 'capacity':TextInput(attrs={'class':'form-control'}),
                 'session_count':TextInput(attrs={'class':'form-control'}),
                 'size':TextInput(attrs={'class':'form-control'}),
                 'status':Select(attrs={'class':'form-control'}),

                }
        labels = {
                'name':u'名称',
                'start_date':u'启用日期',
                'is_started':u'是否启用',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'代码',
                'install_date':u'安装日期',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',
                'battery_type':u'电池类型',
                'capacity':u'电池容量',
                'session_count':u'电池组节数',
                'size':u'尺寸规格',
                'status':u'电池组状态',
                }

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
                 'status':Select(attrs={'class':'form-control'}),
                 'install_date':DateInput(attrs={'class':'form-control'}),

                 'gateway':TextInput(attrs={'class':'form-control'}),
                 'gateway_address':TextInput(attrs={'class':'form-control'}),
                 'netcard_sn':TextInput(attrs={'class':'form-control'}),
                 'configuration':TextInput(attrs={'class':'form-control'}),
                }
        labels = {
                'start_date':u'启用日期',
                'manufacturer':u'设备厂家',
                'specification':u'规格型号',
                'code':u'UPS编号',
                'name':u'名称',
                'asset_id':u'资产编号',
                'equipment_life':u'设备使用年限',
                'phone':u'厂家联系电话',
                'maintenance_cycles':u'维保周期',
                'maintenance_unit':u'代维单位',
                'is_monitoring':u'是否监控',
                'machine_room':u'所属机房',
                'status':u'UPS状态',
                'install_date':u'安装日期',
                'gateway':u'UPS网关',
                'gateway_address':u'UPS网关地址',
                'netcard_sn':u'UPS网卡序列号',
                'configuration':u'配置情况',
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
        labels = {
                'room_id':u'机房ID',
                'room_type':u'机房类型',
                'area':u'所属区域',
                'name':u'名称',
                'address':u'地址',
                'cover_range':u'覆盖范围',
                'is_all_net':u'是否全网',
                'phone':u'联系电话',
                'room_status':u'状态',
                'start_date':u'启用日期',
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
admin.site.register(IPAddress)
admin.site.register(IPBussinessType)

