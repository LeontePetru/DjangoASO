from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from chatapp.models import Room, ChatRoomParticipant, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')

def roomList(request, user):
    return render(request, 'roomSelector.html', {
        'username': user,
    })

def room(request,room,username):
    room_details = Room.objects.get(roomName=room)
    return render(request, 'chatRoom.html', {
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
    roomName = request.POST['roomName']
    username = request.POST['username']

    if Room.objects.filter(roomName=roomName).exists():
        return redirect('/room/' + roomName + '/' + username)
    else:
        new_room = Room.objects.create(roomName=roomName)
        new_room.save()
        return redirect('/room/' + roomName + '/' + username)

def getUserRooms(request, user):
    user_details = User.objects.get(username=user)
    rooms = ChatRoomParticipant.objects.filter(user=user_details.username)
    return JsonResponse({"rooms":list(rooms.values())})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(text=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(roomName=room)

    messages = Message.objects
    return JsonResponse({"messages":list(messages.values())})

