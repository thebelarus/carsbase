from django.urls import path, include
from . import views
urlpatterns = [
    path('brand/<str:manufacture>/', views.get_all_cars_by_manufacture, name='by_manufacture'),
    path('color/<str:color>/', views.get_all_cars_by_color, name='by_color'),
    path('new/car/', views.add_car, name='add_car'),
    path('new/color/', views.add_color, name='add_color'),
    path('new/manufacture/', views.add_manufacture, name='add_manufacture'),
    path('new/body/', views.add_body, name='add_body'),
    path('new/fueltype/', views.add_fueltype, name='add_fueltype'),
    path('', views.get_all_cars, name='all_cars'),
]
