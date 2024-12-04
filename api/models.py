from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)  
    imagen = models.URLField(max_length=100)  
    año = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=200)  
