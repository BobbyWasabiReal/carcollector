from django.shortcuts import render

cars = [
    {'make': 'Toyota', 'model': 'Supra', 'year': 1997, 'description': 'A JDM classic, loved by all!'},
    {'make': 'Toyota', 'model': 'MR2', 'year': 1996, 'description': "The Totyota MR2 is a mid-engine, 4 cylinder, light-weight track beast from the 90's!"},
    {'make': 'Mazda', 'model': 'Miata', 'year': 1990, 'description': "The legendary Mazda Miata. Do not underestimate the cute looks of the Miata! Because the Miata is a light-weight, affordable, and fun daily driver!"},
]


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {
        'cars': cars
    })