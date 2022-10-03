from django.db import models

# Create your models here.

class Contactos(models.Model):
    email= models.EmailField()
    nombre= models.CharField(max_length=30)
    contactotelefonico= models.IntegerField()
    mensaje = models.CharField(max_length=1000)

    def __str__(self):
        return f"nombre: {self.nombre} - email: {self.nombre}"



class jugadoresSelecciones(models.Model):
    pais = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()
    posicion = models.CharField(max_length=30)

    def __str__(self):
        return f"Pais: {self.pais} - Jugador: {self.nombre} {self.apellido}"