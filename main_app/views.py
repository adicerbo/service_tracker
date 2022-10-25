from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Boat, Part
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServiceForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
    boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })

def boats_detail(request, boat_id):
    boat = Boat.objects.get(id=boat_id)
    parts_boat_doesnt_have = Part.objects.exclude(
        id__in=boat.parts.all().values_list('id')
    )
    service_form = ServiceForm()
    return render(request, 'boats/detail.html', {
        'boat': boat, 
        'service_form': service_form,
        'parts': parts_boat_doesnt_have
        })

def add_service(request, boat_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.boat_id = boat_id
        new_service.save()
    return redirect('detail', boat_id=boat_id)

def assoc_part(request, boat_id, part_id):
    Boat.objects.get(id=boat_id).parts.add(part_id)
    return redirect('detail', boat_id=boat_id)

class BoatCreate(CreateView):
    model = Boat
    fields = ['name', 'brand', 'num_engines', 'engine', 'drive_type', 'length', 'generator', 'year', 'hours']
    success_url = '/boats/'

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['hours']

class BoatDelete(DeleteView):
    model = Boat
    success_url = '/boats/'

class PartCreate(CreateView):
    model = Part
    fields = '__all__'
    
class PartUpdate(UpdateView):
    model = Part
    fields = '__all__'

class PartDelete(DeleteView):
    model = Part
    success_url = '/parts/'

class PartDetail(DetailView):
    model = Part
    template_name = 'parts/detail.html'

class PartList(ListView):
    model = Part
    template_name = 'parts/index.html'