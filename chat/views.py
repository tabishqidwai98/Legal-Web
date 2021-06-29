from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.models import Client, Lawyer

# Create your views here.
@login_required
def index(request):
    if request.user.is_client or request.user.is_superuser:
        lawyers = Lawyer.objects.all()
        ctx = {
            'chat_header':'What chat room would you like to enter?',
            'people':lawyers
        }
        return render(request,'chat/index.html',ctx)
    elif request.user.is_lawyer:
        # kya lawyer client se chat krega apni marzi se?
        # because this is stupid
        clients = Lawyer.objects.all()
        ctx = {
            'chat_header':'Chat with your clients.',
            'people':clients
        }
        return render(request,'chat/index.html',ctx)
    
  
@login_required
def room(request,room_name):
    ctx = {
        'room_name': room_name
    }
    return render(request, 'chat/room.html',ctx )

