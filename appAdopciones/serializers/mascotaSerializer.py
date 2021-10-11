from appAdopciones.models.mascotas import Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['Nombre', 'Edad', 'Disponibilidad']

    def to_representation(self, obj):
        mascota = Mascotas.objects.get(id=obj.id)
        
        return{
            'Nombre': mascota.Nombre,
            'Edad' : mascota.Edad,
            'Disponibilidad' : mascota.Disponibilidad
            }
       