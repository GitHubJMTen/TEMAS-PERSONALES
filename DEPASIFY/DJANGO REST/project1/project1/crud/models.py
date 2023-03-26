from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
           
# Create your models here.

class datoscrud(models.Model):
    Nombre=models.CharField(max_length=100)
    Apellidos=models.CharField(max_length=100)
    Calificacion=models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    FechaHoraCreacion=models.DateTimeField(auto_now_add=True)