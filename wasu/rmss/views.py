from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from rmss.models import MachineRoom
# Create your views here.
def machine_room_view(request):
    pass

def machine_room_list_view(request):
    page = request.GET.get('page','1')
    item_list = MachineRoom.objects.all()
    paginator = DiggPaginator(item_list,100,body=5, padding=2)
    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)

    
    return render_to_response('machine_room_list.html',{'items':m},context_instance=RequestContext(request)) 

def machine_room_add_view(request):
    pass

def machine_room_delete_view(request):
    pass
