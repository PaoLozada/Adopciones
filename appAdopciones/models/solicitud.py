from django.db import models
from .user import User
from .candidatos import Candidatos
from .mascotas import Mascotas

class Solicitud(models.Model):
    id_Solicitud = models.AutoField(primary_key=True)
    id_User = models.ForeignKey(User, related_name='solicitud', on_delete=models.CASCADE)
    id_Mascotas = models.ForeignKey(Mascotas, related_name='id_Mascotas', on_delete=models.CASCADE)
    id_Candidatos = models.ForeignKey(Candidatos, related_name='id_Candidatos', on_delete=models.CASCADE)
    estado = models.CharField('estado', max_length=20)
    respuesta = models.CharField('respuesta', max_length=50)