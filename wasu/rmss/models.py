from django.db import models
from wasu.settings import *
# Create your models here.
class Selection(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class MachineRoomType(Selection):
    pass

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
    start_date = models.DateField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '[%s]%s'%(self.room_id, self.name)
    
class Equipment(models.Model):
    start_date = models.DateField(auto_now=True,auto_now_add=True)
    is_started = models.BooleanField()
    manufacturer = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    install_date = models.DateField(auto_now=True,auto_now_add=True)
    asset_id = models.CharField(max_length=100)
    equipment_life = models.IntegerField()
    phone = models.CharField(max_length=100)
    maintenance_cycles = models.CharField(max_length=100)
    maintenance_unit = models.CharField(max_length=100)

    is_monitoring = models.CharField(max_length=100, choices= MONIROTING_CHOICES,default=NO)

    machine_room = models.ForeignKey(MachineRoom)

    def __unicode__(self):
        return '%s %s' % (self.machine_room.name,self.name)

class UPS(Equipment):
    gateway = models.CharField(max_length=100)
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

    switch_gear_cabinet = models.ForeignKey(SwitchGearCabinet)

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
