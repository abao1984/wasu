from django.db import models
from wasu.settings import *
from django.contrib.auth.models import User
# Create your models here.
class Selection(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class MachineRoomType(Selection):
    pass
    
    def __unicode__(self):
        return self.name

class MachineRoomUsage(Selection):
    pass

class Area(Selection):
    pass
    
    def __unicode__(self):
        return self.name

class MachineRoom(models.Model):
    room_id = models.CharField(max_length=20, unique=True)
    room_type = models.ForeignKey(MachineRoomType)
    area = models.ForeignKey(Area)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    cover_range = models.TextField(blank=True)
    is_all_net = models.BooleanField()
    remark = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    room_status = models.CharField(max_length=100,choices=MACHINE_ROOM_CHOICES,default=ENABLE)
    start_date = models.DateField(blank=True)

    def __unicode__(self):
        return '[%s]%s'%(self.room_id, self.name)
    
class Equipment(models.Model):
    start_date = models.DateField()
    is_started = models.BooleanField()
    manufacturer = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    install_date = models.DateField()
    asset_id = models.CharField(max_length=100)
    equipment_life = models.IntegerField()
    phone = models.CharField(max_length=100)
    maintenance_cycles = models.CharField(max_length=100)
    maintenance_unit = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=ENABLE)

    is_monitoring = models.CharField(max_length=100, choices= MONIROTING_CHOICES,default=NO,blank=True)

    machine_room = models.ForeignKey(MachineRoom)

    def __unicode__(self):
        return '%s-%s' % (self.machine_room.name,self.name)

class UPS(Equipment):
    gateway = models.CharField(max_length=100)
    gateway_address = models.CharField(max_length=100)
    netcard_sn = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s %s' % (self.machine_room.name,self.name)

class Battery(Equipment):
    battery_type = models.CharField(max_length=100,choices=BATTERY_TYPE_CHOICES ,default=AC)
    capacity = models.CharField(max_length=100)
    session_count = models.IntegerField()
    size = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s %s' % (self.machine_room.name,self.name)

class AirConditioning(Equipment):
    pass

class SwitchGearCabinet(Equipment):
    power_supply = models.CharField(max_length=100,choices=POWER_SUPPLY_CHOICES,default=SINGLE)
    oil_machine_interface = models.CharField(max_length=100,choices=INTERFACE_CHOICES,default=NOT_HAVE)
    lightning_protection = models.CharField(max_length=100, choices=INTERFACE_CHOICES, default=NOT_HAVE)
    ammeter = models.CharField(max_length=100, choices=INTERFACE_CHOICES, default=NOT_HAVE)
    ammeter_magnification = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s %s' % (self.machine_room.name,self.name)

class AirSwitch(models.Model):
    name = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100,choices=AIR_SWITCH_CONFIGURATION_CHOICES,default=A10)
    total_count = models.IntegerField()
    used_count = models.IntegerField()
    switch_gear_cabinet = models.ForeignKey(SwitchGearCabinet)
    remark = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s %s' % (self.gear.machine_room.name, self.gear.name,self.name)

class ColumnHeadCabinet(SwitchGearCabinet):
    pass

class DistributionCabinet(SwitchGearCabinet):
    pass

class MonitorEquipment(Equipment):
    pass

class EntranceGuardEquipment(Equipment):
    pass

class FirefightingEquipment(Equipment):
    pass

class Client(models.Model):
    pass

class AbstractIP(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

    class Meta:
        abstract = True

class MyUser(models.Model):
    user = models.OneToOneField(User) 
    department = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username

class IPBussinessType(Selection):
    pass

class IPAddress(AbstractIP):
    address = models.IPAddressField(max_length=100)
    subnet_mask = models.IPAddressField(max_length=100) 
    machine_room = models.ForeignKey('MachineRoom',blank=True,null=True)
    remark = models.TextField(blank=True)
    bussiness_type = models.ForeignKey('IPBussinessType', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ENABLE)
    max_host_count = models.IntegerField()
    record_user = models.ForeignKey('MyUser', related_name='record_user')
    record_date = models.DateField(auto_now=True, auto_now_add=True)
    change_user = models.ForeignKey('MyUser', related_name='change_user',blank=True,null=True)
    change_date = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.address
   
class DeviceType(Selection):
    pass

    def __unicode__(self):
        return self.name

class SlotType(Selection):
    pass

    def __unicode__(self):
        return self.name

class PortType(Selection):
    pass

    def __unicode__(self):
        return self.name

class PortSpeed(Selection):
    pass
    
    def __unicode__(self):
        return self.name

class DeviceTemplate(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.ForeignKey('DeviceType')
    model_name = models.CharField(max_length=100)
    has_slot = models.BooleanField()
    slot_count = models.IntegerField()
    port_count = models.IntegerField()

    def __unicode__(self):
        return self.name

class AbstractSlotInfo(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        abstract = True

class SlotInfo(models.Model):
    slot_type = models.ForeignKey('SlotType')
    is_used = models.BooleanField()
    card_model = models.CharField(max_length=100)
    slot_number = models.IntegerField()
    device_template = models.ForeignKey('DeviceTemplate')

    def __unicode__(slef):
        return '%s-%s' %(self.device_template.name,self.slot_number)

class PortInfo(models.Model):
    is_used = models.BooleanField()
    speed = models.ForeignKey('PortSpeed')
    port_type = models.ForeignKey('PortType')
    is_multiply = models.BooleanField()
    port_number = models.IntegerField()
    device_template = models.ForeignKey('DeviceTemplate')

    def __unicode__(self):
        return '%s-%s' % (self.device_template.name, self.port_number)
