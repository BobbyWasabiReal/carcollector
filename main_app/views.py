from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
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
    mod_form = ModForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'mod_form': mod_form
    })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

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