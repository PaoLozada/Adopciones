from appAdopciones.models.mascotas import Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['Nombre', 'Edad', 'Disponibilidad']   

    

    def to_representation(self, obj):
        Mascota = Mascotas.objects.get(id=obj.id)
        
        
        return{
            'Nombrecito': Mascota.Nombre,
            'Edadcita': Mascota.Edad,
            'Disponibilidadcita': Mascota.Disponibilidad

        }
        

    
       