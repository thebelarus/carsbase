from django.forms import ModelForm
from . import models

class CarForm(ModelForm):
	class Meta:
		model = models.Car
		fields = ('model','body','color','fuel_type')
