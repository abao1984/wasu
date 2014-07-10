from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext

# Create your views here.
def machine_room_view(request):
    pass

def machine_room_list_view(request):
    return render_to_response('base.html',{},context_instance=RequestContext(request)) 

def machine_room_add_view(request):
    pass

def machine_room_delete_view(request):
    pass
