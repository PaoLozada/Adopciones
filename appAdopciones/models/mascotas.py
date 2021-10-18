from django.db import models


class Mascotas(models.Model):
    Id_Mascota = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre', max_length=50)
    Edad = models.IntegerField('Edad')
    Disponibilidad = models.CharField('Disponibilidad',max_length=2)  


    