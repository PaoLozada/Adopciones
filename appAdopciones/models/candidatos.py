from django.db import models


class Candidatos(models.Model):
    Id_Candidato = models.AutoField(primary_key=True)
    Numero_Identificacion = models.CharField('Numero_Identificacion', max_length=20)
    Nombre_Completo = models.CharField('Nombre_Completo', max_length=50)
    Direccion = models.CharField('Direccion', max_length=30)
    Numero_Contacto = models.CharField('Numero_Contacto', max_length=20)
    Email = models.CharField('Email', max_length=30)
    Edad = models.IntegerField('Edad')
    Has_Tenido_Mascotas = models.CharField('Ha_Tenido_Mascotas', max_length=2, null=True)
    Seras_Responsable = models.CharField('Seras_Responsable', max_length=2, null=True)
    Tienes_Espacio = models.CharField('Tienes_Espacio', max_length=2, null=True)
    Tienes_Tiempo = models.CharField('Tienes_Tiempo', max_length=2, null=True)
    Recursos_Economicos = models.CharField('Recursos_Economicos', max_length=2, null=True)
    Afrontar_Problemas = models.CharField('Afrontar_Problemas', max_length=2, null=True)
    Resultado_Prueba = models.IntegerField('Resultado_Prueba', default= False)  


   