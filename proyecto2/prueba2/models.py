from django.db import models

# Create your models here.

#aviones clase o la clase creada tiene que tener  la primra letra en mayuscula
class Avion(models.Model):
     nombre = models.CharField(max_length=60)
     fabricante = models.CharField(max_length=40)
     cantidaddemotores = models.IntegerField(default=1)
     
     #con esto me muestra en el admin el nombre asignado en la tabla
     def __str__(self) -> str:
          return "Avion" + "  " + self.fabricante + "  " + self.nombre + "  " + str(self.cantidaddemotores)
