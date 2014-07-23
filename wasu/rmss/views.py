from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext
from rmss.models import MachineRoom, UPS, Battery
from dig_paginator import DiggPaginator
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from rmss.admin import MachineRoomForm, UPSForm, BatteryForm
from django.http import HttpResponse
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

