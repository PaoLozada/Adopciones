from django.db import models


class Mascotas(models.Model):
    Id_Mascota = models.CharField(primary_key=True,max_length=20)
    Nombre = models.CharField('Nombre', max_length=50)
    Edad = models.IntegerField(default=0)
    Disponibilidad = models.BooleanField(default=True)


    