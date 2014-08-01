from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext
from rmss.models import * 
from dig_paginator import DiggPaginator
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from rmss.admin import * 
from django.http import HttpResponse
from django.core import serializers
import simplejson
# Create your views here.
def rmss_response(request,dic,template):
    return render_to_response(template,dic,context_instance=RequestContext(request))

def machine_room_detail_view(request,id):
    instance = get_object_or_404(MachineRoom, id=id)
    if request.POST:
        form = MachineRoomForm(request.POST,instance=instance)
        if form.is_valid():
            room = form.save()
    else:
        form = MachineRoomForm(instance=instance)
    return rmss_response(request,{'form':form,'id':id}, 'machine_room_detail.html')

def machine_room_list_view(request):
    page = request.GET.get('page','1')
    item_list = MachineRoom.objects.all()
    paginator = DiggPaginator(item_list,10,body=5, padding=2)
    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)
    return rmss_response(request, {'items':rooms}, 'machine_room_list.html')    

def machine_room_add_view(request):
    if request.POST:
        instance = MachineRoom()
        form = MachineRoomForm(request.POST,instance=instance)
        if form.is_valid():
            machine_room = form.save()
            return redirect('rmss.views.machine_room_detail_view', id=machine_room.id)
        else:
            return rmss_response(request,{'form':form}, 'machine_room_add.html')
    form = MachineRoomForm()
    return rmss_response(request,{'form':form},'machine_room_add.html')

def machine_room_advance_search_view(request):
    pass

def machine_room_delete_view(request, id):
    instance = get_object_or_404(MachineRoom,id=id)
    instance.delete()
    return redirect('rmss.views.machine_room_list_view')

def ups_add_view(request,room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    if request.POST:
        instance = UPS()
        instance.machine_room = room
        form = UPSForm(request.POST, instance=instance)
        if form.is_valid():
            ups = form.save()
            return redirect('rmss.views.ups_list_view',room_id=room_id)
        else:
            return redirect('rmss.views.ups_list_view',room_id=room_id)
    form = UPSForm()
    return rmss_response(request,{'form':form,'room':room},'ups_add.html') 

def ups_list_view(request, room_id):
    room = get_object_or_404(MachineRoom,id=room_id)
    items = UPS.objects.filter(machine_room=room)
    return rmss_response(request,{'items':items,'room':room},'ups_list.html')

def ups_detail_view(request,room_id, ups_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    ups = get_object_or_404(UPS,id = ups_id)
    form = UPSForm(instance=ups)
    if request.POST:
        form = UPSForm(request.POST, instance=ups)
        return redirect('rmss.views.ups_list_view',room_id=room_id)
    return rmss_response(request,{'form':form,'room':room, 'ups':ups},'ups_detail.html')

def battery_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    items = Battery.objects.filter(machine_room=room)
    return rmss_response(request, {'items':items, 'room':room},'battery_list.html')

def battery_add_view(request, room_id):
    room = get_object_or_404(MachineRoom,id=room_id)
    if request.POST:
        instance = Battery()
        instance.machine_room = room
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = BatteryForm(default_data, instance=instance)
        if form.is_valid():
            battery = form.save()
            return redirect('rmss.views.battery_list_view', room_id=room_id)
        print '@97',form.errors
        return rmss_response(request, {'form':form, 'room':room}, 'battery_add.html')
    else:
        form = BatteryForm()
        return rmss_response(request, {'form':form, 'room':room}, 'battery_add.html')

def battery_detail_view(request,room_id, battery_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    battery = get_object_or_404(Battery, id=battery_id)
    form = BatteryForm(instance=battery)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = BatteryForm(default_data, instance=battery)
        print '@109',form.errors 
        if form.is_valid():
            battery = form.save()
            return redirect('rmss.views.battery_list_view',room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room, 'battery':battery}, 'battery_detail.html')

def ac_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    items = AirConditioning.objects.filter(machine_room=room)
    return rmss_response(request, {'items':items, 'room':room},'ac_list.html')

def ac_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    if request.POST:
        instance = AirConditioning()
        instance.machine_room = room
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = ACForm(default_data, instance=instance)
        if form.is_valid():
            ac = form.save()
            return redirect('rmss.views.ac_list_view', room_id=room_id)
        else:
            return rmss_response(request, {'form':form, 'room':room},'ac_add.html')
    else:
        form = ACForm()
        return rmss_response(request, {'form':form, 'room':room},'ac_add.html')

def ac_detail_view(request, room_id, ac_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    ac = get_object_or_404(AirConditioning, id=ac_id)
    form = ACForm(instance=ac)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = ACForm(default_data, instance=ac)
        if form.is_valid():
            ac  = form.save()
            return redirect('rmss.views.ac_list_view', room_id=room_id)
    return rmss_response(request,{'form':form, 'room':room, 'ac':ac}, 'ac_detail.html')

def power_cabinet_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    switch_gears = SwitchGearCabinet.objects.filter(machine_room=room)
    column_heads = ColumnHeadCabinet.objects.filter(machine_room=room) 
    distributions = DistributionCabinet.objects.filter(machine_room=room)
    return rmss_response(request,{'items1':switch_gears,'items2':column_heads,'items3':distributions,'room':room}, 'power_cabinet_list.html')

def switch_gear_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    if request.POST:
        instance = SwitchGearCabinet()
        instance.machine_room = room
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = SwitchGearCabinetForm(default_data, instance=instance)
        if form.is_valid():
            s = form.save()
            return redirect('rmss.views.power_cabinet_list_view',room_id)
        else:
            return rmss_response(request,{'form':form, 'room':room},'switch_gear_add.html')
    else:
        form = SwitchGearCabinetForm()
        return rmss_response(request,{'form':form, 'room':room},'switch_gear_add.html')

def switch_gear_detail_view(request, room_id, cabinet_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    cabinet = get_object_or_404(SwitchGearCabinet, id=cabinet_id)
    form = SwitchGearCabinetForm(instance=cabinet)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = SwitchGearCabinetForm(default_data, instance=cabinet)
        if form.is_valid():
            cabinet = form.save()
            return redirect('rmss.views.power_cabinet_list_view', room_id)
    airswitch_list = AirSwitch.objects.filter(switch_gear_cabinet=cabinet)
    return rmss_response(request, {'form':form, 'room':room,'cabinet_id':cabinet_id,'airswitch_list':airswitch_list}, 'switch_gear_detail.html')

def column_head_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    if request.POST:
        instance = ColumnHeadCabinet()
        instance.machine_room = room
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = ColumnHeadCabinetForm(default_data, instance=instance)
        if form.is_valid():
            s = form.save()
            return redirect('rmss.views.power_cabinet_list_view',room_id)
        else:
            return rmss_response(request,{'form':form, 'room':room},'column_head_add.html')
    else:
        form = ColumnHeadCabinetForm()
        return rmss_response(request,{'form':form, 'room':room},'column_head_add.html')

def column_head_detail_view(request, room_id, cabinet_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    cabinet = get_object_or_404(ColumnHeadCabinet, id=cabinet_id)
    form = ColumnHeadCabinetForm(instance=cabinet)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = ColumnHeadCabinetForm(default_data, instance=cabinet)
        if form.is_valid():
            cabinet = form.save()
            return redirect('rmss.views.power_cabinet_list_view', room_id)
    airswitch_list = AirSwitch.objects.filter(switch_gear_cabinet=cabinet)
    return rmss_response(request, {'form':form, 'room':room,'cabinet_id':cabinet_id,'airswitch_list':airswitch_list}, 'column_head_detail.html')

def distribution_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    if request.POST:
        instance = DistributionCabinet()
        instance.machine_room = room
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = DistributionCabinetForm(default_data, instance=instance)
        if form.is_valid():
            s = form.save()
            return redirect('rmss.views.power_cabinet_list_view',room_id)
        else:
            return rmss_response(request,{'form':form, 'room':room},'distribution_add.html')
    else:
        form = DistributionCabinetForm()
        return rmss_response(request,{'form':form, 'room':room},'distribution_add.html')

def distribution_detail_view(request, room_id, cabinet_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    cabinet = get_object_or_404(DistributionCabinet, id=cabinet_id)
    form = DistributionCabinetForm(instance=cabinet)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = DistributionCabinetForm(default_data, instance=cabinet)
        if form.is_valid():
            cabinet = form.save()
            return redirect('rmss.views.power_cabinet_list_view', room_id)
    airswitch_list = AirSwitch.objects.filter(switch_gear_cabinet=cabinet)
    return rmss_response(request, {'form':form, 'room':room,'cabinet_id':cabinet_id,'airswitch_list':airswitch_list}, 'distribution_detail.html')

def airswitch_add_view(request, room_id, cabinet_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    cabinet = get_object_or_404(SwitchGearCabinet, id=cabinet_id)
    if request.POST:
        instance = AirSwitch()
        instance.switch_gear_cabinet = cabinet
        default_data = request.POST.copy()
        default_data["switch_gear_cabinet"] = cabinet.id
        form = AirSwitchForm(default_data, instance=instance)
        if form.is_valid():
            air_switch = form.save()
            return redirect('rmss.views.switch_gear_detail_view', room.id, cabinet_id)
        else:
            return rmss_response(request, {'form':form,'room':room, 'cabinet':cabinet}, 'airswitch_add.html')
    else:
        form = AirSwitchForm()
        return rmss_response(request, {'form':form, 'room':room, 'cabinet':cabinet}, 'airswitch_add.html')
        
def airswitch_detail_view(request, room_id, cabinet_id, airswitch_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    cabinet = get_object_or_404(SwitchGearCabinet, id=cabinet_id)
    airswitch = get_object_or_404(AirSwitch, id=airswitch_id)
    form  = AirSwitchForm(instance=airswitch)
    if request.POST:
        default_data = request.POST.copy()
        default_data['switch_gear_cabinet'] = cabinet_id
        form = AirSwitchForm(default_data,instance=airswitch)
        if form.is_valid():
            airswitch = form.save()
            return redirect('rmss.views.switch_gear_detail_view', room.id,cabinet_id)
    return rmss_response(request,{'form':form,'room':room, 'cabinet':cabinet}, 'airswitch_detail.html')
        
def monitor_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    items = MonitorEquipment.objects.filter(machine_room=room)
    return rmss_response(request, {'room':room,'items':items},'monitor_list.html')

def monitor_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    form = MonitorEquipmentForm()
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        instance = MonitorEquipment()
        form = MonitorEquipmentForm(default_data, instance=instance)
        if form.is_valid():
            monitor = form.save()
            return redirect('rmss.views.monitor_list_view', room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room}, 'monitor_add.html')

def monitor_detail_view(request, room_id, monitor_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    monitor = get_object_or_404(MonitorEquipment, id=monitor_id)
    form = MonitorEquipmentForm(instance=monitor)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form = MonitorEquipmentForm(default_data, instance=monitor)
        if form.is_valid():
            monitor = form.save()
            return redirect('rmss.views.monitor_list_view', room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room, 'monitor':monitor}, 'monitor_detail.html')

def entrance_guard_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    items = EntranceGuardEquipment.objects.filter(machine_room=room)
    return rmss_response(request, {'room':room, 'items':items},'entrance_guard_list.html')

def entrance_guard_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    form = EntranceGuardEquipmentForm()
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        instance = EntranceGuardEquipment()
        form = EntranceGuardEquipmentForm(default_data, instance=instance)
        if form.is_valid():
            eg = form.save()
            return redirect('rmss.views.entrance_guard_list_view', room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room}, 'entrance_guard_add.html')

def entrance_guard_detail_view(request, room_id,entrance_guard_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    eg = get_object_or_404(EntranceGuardEquipment, id=entrance_guard_id)
    form = EntranceGuardEquipmentForm(instance=eg)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        form  = EntranceGuardEquipmentForm(default_data, instance=eg)
        if form.is_valid():
            eg = form.save()
            return redirect('rmss.views.entrance_guard_list_view', room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room, 'entrance_guard':eg}, 'entrance_guard_detail.html')

def fire_fight_list_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    items = FirefightingEquipment.objects.filter(machine_room=room)
    return rmss_response(request, {'room':room, 'items':items}, 'fire_fight_list.html')

def fire_fight_add_view(request, room_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    form = FirefightingEquipmentForm()
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] = room_id
        instance = FirefightingEquipment()
        form = FirefightingEquipmentForm(default_data, instance=instance)
        if form.is_valid():
            fire_fight = form.save()
            return redirect('rmss.views.fire_fight_list_view', room_id=room_id)
    return rmss_response(request, {'form':form, 'room':room}, 'fire_fight_add.html')

def fire_fight_detail_view(request, room_id, fire_fight_id):
    room = get_object_or_404(MachineRoom, id=room_id)
    ff = get_object_or_404(FirefightingEquipment, id=fire_fight_id)
    form = FirefightingEquipmentForm(instance=ff)
    if request.POST:
        default_data = request.POST.copy()
        default_data['machine_room'] =room_id
        form = FirefightingEquipmentForm(default_data, instance=ff)
        if form.is_valid():
            ff = form.save()
            return redirect('rmss.views.fire_fight_list_view', room_id=room_id)
    return rmss_response(request, {'room':room, 'form':form, 'fire_fight':ff}, 'fire_fight_detail.html')

def machine_room_search_view(request):
    rooms = MachineRoom.objects.all()
    data = serializers.serialize('json', rooms, ensure_ascii=False, indent=4,separators=(',\n', ':'), fields=('room_id','name','room_type'))
#    json_str = simplejson.dumps(data,ensure_ascii=False, indent=4,separators=(',\n',':'))
    return HttpResponse(data, content_type="application/json")

def ip_add_view(request):
    form = IPAddressForm()
    if request.POST:
        default_data = request.POST.copy()
        form = IPAddressForm(default_data)
        default_data['record_user'] = request.user
        if form.is_valid():
            ip = form.save()
            return redirect('rmss.views.ip_list_view')
    return rmss_response(request, {'form':form}, 'ip_add.html')

def ip_detail_view(request,ip_id):
    ip = get_object_or_404(IPAddress, id=ip_id)
    form = IPAddressForm(instance=ip)
    if request.POST:
        default_data = request.POST.copy()
        default_data['change_user'] = request.user
        form = IPAddressForm(default_data,instance=ip) 
        if form.is_valid():
            ip = form.save()
            return redirect('rmss.views.ip_list_view')
    return rmss_response(request, {'form':form, 'ip':ip},ip_detail.html)

def ip_list_view(request):
    pass
