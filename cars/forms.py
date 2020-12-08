from django.forms import ModelForm
from . import models

class CarForm(ModelForm):
	class Meta:
		model = models.Car
		fields = ('model','manufacture','body','color','fuel_type')

class ManufactureForm(ModelForm):
	class Meta:
		model = models.Manufacture
		fields = ('name',)

class BodyForm(ModelForm):
	class Meta:
		model = models.Body
		fields = ('name',)

class ColorForm(ModelForm):
	class Meta:
		model = models.Color
		fields = ('name',)

class FuelType(ModelForm):
	class Meta:
		model = models.FuelType
		fields = ('name',)
