from django.shortcuts import render, redirect
from .models import Boat
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
    boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })

def boats_detail(request, boat_id):
    boat = Boat.objects.get(id=boat_id)
    return render(request, 'boats/detail.html', {'boat': boat})

def add_services(request, boat_id):
    form = ServicesForm(request.POST)
    if form.is_valid():
        new_services = form.save(commit=FALSE)
        new_services.boat_id = boat_id
        new_services.save()
    return redirect('detail', boat_id=boat_id)

class BoatCreate(CreateView):
    model = Boat
    fields = '__all__'
    success_url = '/boats/'

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['hours']

class BoatDelete(DeleteView):
    model = Boat
    success_url = '/boats/'