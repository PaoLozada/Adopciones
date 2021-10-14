from appAdopciones.models.mascotas import Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['Id_Mascota','Nombre','Edad','Disponibilidad']   

    
    '''def create (self, validated_data):
        mascotaInstance = Mascotas.objects.create(**validated_data)
        return mascotaInstance'''

        

    def to_representation(self, obj):
        mascota = Mascotas.objects.get()
        
        
        return{
            'Nombrecito': mascota.Nombre,
            'Edadcita': mascota.Edad,
            'Disponibilidadcita': mascota.Disponibilidad

        }
        

    
       