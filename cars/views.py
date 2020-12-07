from django.shortcuts import render
from . import models
from . import forms

def get_all_cars(request):
    cars = models.Car.objects.all()
    manufacture_all =  models.Manufacture.objects.all() 
    context = {'cars':cars,'manufactures':manufacture_all}
    return render(request, 'base.html', context)

def get_all_cars_by_manufacture(request, manufacture):
    manufacture =  models.Manufacture.objects.get(name=manufacture) 
    manufacture_all =  models.Manufacture.objects.all() 
    models_ = models.Model.objects.filter(manufacture=manufacture)
    cars = models.Car.objects.filter(model__in=models_)
    context = {'cars':cars,'manufactures':manufacture_all}
    return render(request, 'base.html', context)

def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
    # manufacture =  models.Manufacture.objects.get(name=manufacture) 
    # manufacture_all =  models.Manufacture.objects.all() 
    # models_ = models.Model.objects.filter(manufacture=manufacture)
    # cars = models.Car.objects.filter(model__in=models_)
    # context = {'cars':cars,'manufactures':manufacture_all}
    else:
        form_class = forms.CarForm
        context = {'form':form_class}
        return render(request, 'car_add.html', context)


# def userDetails(request):

#     if request.method == 'POST':
#         form = UserModelForm(request.POST)
#         if form.is_valid():

#             u = form.save()
#             users = UserDetails.objects.all()

#             return render(request, 'display.html', {'users': users})

            

#     else:
#         form_class = UserModelForm

#     return render(request, 'userdetails.html', {
#         'form': form_class,
#     })    

def get_all_cars_by_color(request, color):
    manufacture =  models.Color.objects.get(name=manufacture) 
    models_ = models.Model.objects.filter(manufacture=manufacture)
    cars = models.Car.objects.filter(model=models_)
    context = {'cars':cars}
    return render(request, 'base.html', context)