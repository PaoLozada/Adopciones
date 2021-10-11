from django.db import models


class Mascotas(models.Model):
    Id_Mascota = models.AutoField(primary_key=True, default=0)
    Nombre = models.CharField('Nombre', max_length=50)
    Edad = models.IntegerField('Edad',default=0)
    Disponibilidad = models.BooleanField('Disponibilidad',default=True)


    