from django.shortcuts import render
from .models import Boat


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
    boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })