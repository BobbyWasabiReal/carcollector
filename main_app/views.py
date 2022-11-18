from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Track
from .forms import ModForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.tracks.all().values_list('id')
    tracks_car_doesnt_have = Track.objects.exclude(id__in=id_list)
    mod_form = ModForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'mod_form': mod_form,
        'tracks': tracks_car_doesnt_have
    })

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'

def add_mod(request, car_id):
    form = ModForm(request.POST)
    if form.is_valid():
        new_mod = form.save(commit=False)
        new_mod.car_id = car_id
        new_mod.save()
    return redirect('detail', car_id=car_id)

class TrackList(ListView):
  model = Track

class TrackDetail(DetailView):
  model = Track

class TrackCreate(CreateView):
    model = Track
    fields = '__all__'

class TrackUpdate(UpdateView):
    model = Track
    fields = ['track', 'location']

class TrackDelete(DeleteView):
    model = Track
    success_url = '/tracks'

def assoc_track(request, car_id, track_id):
    Car.objects.get(id=car_id).tracks.add(track_id)
    return redirect('detail', car_id=car_id)

def unassoc_track(request, car_id, track_id):
    Car.objects.get(id=car_id).tracks.remove(track_id)
    return redirect('detail', car_id=car_id)