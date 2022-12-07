from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from chatapp.models import Room, ChatRoomParticipant
from django.http import HttpResponse, JsonResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')

def roomList(request, user):
    return render(request, 'roomSelector.html', {
        'username': user,
    })

def room(request, room, username):
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkCredentials(request):
    username = request.POST['username']
    password = request.POST['password']

    user= authenticate (username=username, password = password)

    if user is not None:
        return  redirect('/roomList/'+username)

def checkRoom(request):
    room = request.POST['roomName']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/room'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/room/?room='+room+'/?username='+username)

def getUserRooms(request, user):
    user_details = User.objects.get(username=user)
    rooms = ChatRoomParticipant.objects.filter(user=user_details.username)
    return JsonResponse({"rooms":list(rooms.values())})

