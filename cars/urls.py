from django.urls import path, include
from . import views
urlpatterns = [
    path('brand/<str:manufacture>/', views.get_all_cars_by_manufacture, name='by_manufacture'),
    path('color/<str:color>/', views.get_all_cars_by_color, name='by_color'),
    path('add/car/', views.add_car, name='add_car'),
    path('', views.get_all_cars),
]
