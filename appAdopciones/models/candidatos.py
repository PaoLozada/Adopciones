from django.db import models


class Candidatos(models.Model):
    Id_Candidato = models.CharField(primary_key=True,max_length=20)
    Numero_Identificacion = models.CharField('Numero_Identificacion', max_length=20)
    Nombre_Completo = models.CharField('Nombre_Completo', max_length=50)
    Direccion = models.CharField('Direccion', max_length=30)
    Numero_Contacto = models.CharField('Numero_Contacto', max_length=20)
    Email = models.CharField('Email', max_length=30)
    Edad = models.IntegerField(default=0)
    Resutado_Prueba = models.IntegerField(default=0)


   