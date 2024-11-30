from django.shortcuts import render
from django.http import HttpResponse
from .models import Room




def home(request):
    rooms = Room.objects.all()         
    context = {'rooms' : rooms}
    return render(request, 'home.html' , context)

def room(request  , pk):
    room = Room.objects.get(id=pk)
    context = { 'room' : room}
    return render(request , 'room.html' , context)

def Profile(request):
    return HttpResponse('Profile Page')

def Event(request):
    return HttpResponse('Event Page')

def Main(request):
    return HttpResponse('Main Page')

def Jassibhai(request):
    return HttpResponse('Game Changer Player')