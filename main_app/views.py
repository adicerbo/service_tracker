from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Boat, Part
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServiceForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def boats_index(request):
    boats = Boat.objects.filter(user=request.user)
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

@login_required
def add_service(request, boat_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.boat_id = boat_id
        new_service.save()
    return redirect('detail', boat_id=boat_id)

@login_required
def assoc_part(request, boat_id, part_id):
    Boat.objects.get(id=boat_id).parts.add(part_id)
    return redirect('detail', boat_id=boat_id)


class BoatCreate(LoginRequiredMixin, CreateView):
    model = Boat
    fields = ['name', 'brand', 'num_engines', 'engine', 'drive_type', 'length', 'generator', 'year', 'hours']
    success_url = '/boats/'


class BoatUpdate(LoginRequiredMixin, UpdateView):
    model = Boat
    fields = ['hours']


class BoatDelete(LoginRequiredMixin, DeleteView):
    model = Boat
    success_url = '/boats/'


class PartCreate(LoginRequiredMixin, CreateView):
    model = Part
    fields = '__all__'
    

class PartUpdate(LoginRequiredMixin, UpdateView):
    model = Part
    fields = '__all__'


class PartDelete(LoginRequiredMixin, DeleteView):
    model = Part
    success_url = '/parts/'

class PartDetail(DetailView):
    model = Part
    template_name = 'parts/detail.html'

class PartList(ListView):
    model = Part
    template_name = 'parts/index.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # how to create a user form object that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add user to database
            user = form.save()
            # log user in
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # a bad POST or GET, render signup.html with empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
