from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    return render(request, 'login.html')

def rooms(request):
    return render(request,'chatRoom.html')

def checkCredentials(request):
    username = request.POST['username']
    password = request.POST['password']

    user= authenticate (username=username, password = password)

    if user is not None:
        return  redirect('room/')
