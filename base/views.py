from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context = {
        'title' : "My Django App",
        'items' : ['apple' ,' ball' , 'cat'],
        'user' : {
            'name': 'Prem' , 'age' : 16
        }
    }
    return render(request, 'home.html' , context)

def room(request):
    return render(request , 'room.html')

def Profile(request):
    return HttpResponse('Profile Page')

def Event(request):
    return HttpResponse('Event Page')

def Main(request):
    return HttpResponse('Main Page')

def Jassibhai(request):
    return HttpResponse('Game Changer Player')