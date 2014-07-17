from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext
from rmss.models import MachineRoom, UPS
from dig_paginator import DiggPaginator
from rmss.admin import MachineRoomForm, UPSForm
from django.http import HttpResponse
# Create your views here.
def rmss_response(request,dic,template):
    return render_to_response(template,dic,context_instance=RequestContext(request))

def machine_room_detail_view(request,id):
    if request.POST:
        pass
    else:
        instance = get_object_or_404(MachineRoom, id=id)
        form = MachineRoomForm(instance=instance)
        return rmss_response(request,{'form':form}, 'machine_room_detail.html')

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

def machine_room_delete_view(request):
    pass

def ups_add_view(request):
    if request.POST:
        instance = UPS()
        form = UPSForm(request.POST, instance=instance)
        if form.is_valid():
            ups = form.save()
            return redirect('rmss.views.machine_room_detail_view',id=ups.machine_room.id)
        else:
            return redirect('rmss.views.machine_room_detail_view',id=request.POST.get('machine_room',''))
    return HttpResponse('error')
