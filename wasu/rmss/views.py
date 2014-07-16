from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from rmss.models import MachineRoom
from dig_paginator import DiggPaginator
from rmss.admin import MachineRoomForm
# Create your views here.
def rmss_response(request,dic,template):
    return render_to_response(template,dic,context_instance=RequestContext(request))

def machine_room_view(request):
    pass

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
        pass
    form = MachineRoomForm()
    return rmss_response(request,{'form':form},'machine_room_add.html')

def machine_room_delete_view(request):
    pass
