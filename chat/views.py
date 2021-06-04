from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.models import Client, Lawyer

# Create your views here.
@login_required
def index(request):
    if request.user.is_client:
        lawyers = Lawyer.objects.all()
        ctx = {
            'chat_header':'discuss with a lawyer',
            'people':lawyers
        }
        return render(request,'chat/index.html',ctx)
    elif request.user.is_lawyer:
        # kya lawyer client se chat krega apni marzi se?
        # because this is stupid
        clients = Client.objects.all()
        ctx = {
            'chat-header':'chat with client',
            'people':clients
        }
        return render(request,'chat/index.html',ctx)

@login_required
def room(request,room_name):
    ctx = {
        'room_name': room_name
    }
    return render(request, 'chat/room.html',ctx )

