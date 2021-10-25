from appAdopciones.models.mascotas import Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['Id_Mascota','Nombre','Edad','Disponibilidad']   

    
    

    
       