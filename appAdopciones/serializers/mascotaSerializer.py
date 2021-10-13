from appAdopciones.models.mascotas import Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['Id_Mascota','Nombre', 'Edad', 'Disponibilidad']   

    

    '''def to_representation(self, obj):
        Mascota = Mascotas.objects.get(Id_Mascota=obj.Id_Mascota)
        
        
        return{
            'Nombrecito': Mascota.Nombre,
            'Edadcita': Mascota.Edad,
            'Disponibilidadcita': Mascota.Disponibilidad

        }'''
        

    
       