from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django. auth.decorators import login_required
from . import models
from . import forms

def get_all_manufactures():
    return models.Manufacture.objects.all()

def get_all_cars(request):
    cars = models.Car.objects.all()
    context = {'cars':cars,'manufactures':get_all_manufactures()}
    return render(request, 'cars.html', context)

def get_all_cars_by_manufacture(request, manufacture):
    manufacture = get_object_or_404(models.Manufacture, name=manufacture)
    models_ = models.Model.objects.filter(manufacture=manufacture)
    cars = models.Car.objects.filter(model__in=models_)
    context = {'cars':cars,'manufactures':get_all_manufactures()}
    return render(request, 'cars.html', context)

def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        new_car = form.save()
        return redirect('add_car')

    else:
        form_class = forms.CarForm
        context = {'form':form_class, 'manufactures':get_all_manufactures()}
        return render(request, 'add.html', context)

def add_color(request):
    if request.method == 'POST':
        form = forms.ColorForm(request.POST)
        new_color = form.save()
        return redirect('add_color')
    else:
        form_class = forms.ColorForm
        context = {'form':form_class, 'data':models.Color.objects.all()}
        return render(request, 'add.html', context)

def add_manufacture(request):
    if request.method == 'POST':
        form = forms.ManufactureForm(request.POST)
        new_manufacture = form.save()
        return redirect('add_manufacture')
    else:
        form_class = forms.ManufactureForm
        context = {'form':form_class, 'data':models.Manufacture.objects.all()}
        return render(request, 'add.html', context)

def add_body(request):
    if request.method == 'POST':
        form = forms.BodyForm(request.POST)
        new_body = form.save()
        return redirect('add_body')
    else:
        form_class = forms.BodyForm
        context = {'form':form_class, 'data':models.Body.objects.all()}
        return render(request, 'add.html', context)

def add_fueltype(request):
    if request.method == 'POST':
        form = forms.FuelType(request.POST)
        new_fueltype = form.save()
        return redirect('add_fueltype')
    else:
        form_class = forms.FuelType
        context = {'form':form_class, 'data':models.FuelType.objects.all()}
        return render(request, 'add.html', context) 

def get_all_cars_by_color(request, color):
    manufacture =  models.Color.objects.get(name=manufacture) 
    models_ = models.Model.objects.filter(manufacture=manufacture)
    cars = models.Car.objects.filter(model=models_)
    context = {'cars':cars}
    return render(request, 'base.html', context)