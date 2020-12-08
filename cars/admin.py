from django.contrib import admin

from .models import Manufacture, Body, FuelType, Color, Car

class FuelTypeAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_field = ('name',)

class CarAdmin(admin.ModelAdmin):
	list_display = ('model','body','color','fuel_type')
	list_display_links = ('model','body','color','fuel_type')
	search_field = ('model',)	


admin.site.register(Manufacture)
admin.site.register(Body)
admin.site.register(FuelType, FuelTypeAdmin)
admin.site.register(Color)
admin.site.register(Car, CarAdmin)

