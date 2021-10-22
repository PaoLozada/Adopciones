from django.db import models


class Candidatos(models.Model):
    Id_Candidato = models.AutoField(primary_key=True)
    Numero_Identificacion = models.CharField('Numero_Identificacion', max_length=20)
    Nombre_Completo = models.CharField('Nombre_Completo', max_length=50)
    Direccion = models.CharField('Direccion', max_length=30)
    Numero_Contacto = models.CharField('Numero_Contacto', max_length=20)
    Email = models.CharField('Email', max_length=30)
    Edad = models.IntegerField('Edad')
    Has_Tenido_Mascotas = models.IntegerField('Ha_Tenido_Mascotas', null=True)
    Seras_Responsable = models.IntegerField('Seras_Responsable', null=True)
    Tienes_Espacio = models.IntegerField('Tienes_Espacio', null=True)
    Tienes_Tiempo = models.IntegerField('Tienes_Tiempo', null=True)
    Recursos_Economicos = models.IntegerField('Recursos_Economicos', null=True)
    Afrontar_Problemas = models.IntegerField('Afrontar_Problemas',null=True)
    Resultado_Prueba = models.IntegerField('Resultado_Prueba', null=True)  


   