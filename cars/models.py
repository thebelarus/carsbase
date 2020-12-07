from django.db import models

class Manufacture(models.Model):
    name = models.CharField(max_length = 15, unique=True, blank=False)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacture'    
        verbose_name_plural = 'Manufactures'    

class Body(models.Model):
    name = models.CharField(max_length = 15, unique=True, blank=False)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Body'   
        verbose_name_plural = 'Bodys'   
        
class Color(models.Model):
    name = models.CharField(max_length = 15, unique=True, blank=False)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'  
        verbose_name_plural = 'Colors'  

class FuelType(models.Model):
    name = models.CharField(max_length = 15, unique=True, blank=False)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fuel type'  
        verbose_name_plural = 'Fuel types'  
        
class Model(models.Model):
    name = models.CharField(max_length = 20, unique=True, blank=False, verbose_name='model')    
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, verbose_name='manufacture') 

    def __str__(self):
        return str(self.manufacture) + ' ' + str(self.name)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'manufacture'], name='unique model of manufacture')

        ]

class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='model')
    body = models.ForeignKey(Body, on_delete=models.CASCADE, verbose_name='body') 
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color') 
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, verbose_name='fuel type')

    def __str__(self):
        return str(self.model) + ' ' + str(self.body) + ' ' + str(self.color) + ' ' + str(self.fuel_type)    