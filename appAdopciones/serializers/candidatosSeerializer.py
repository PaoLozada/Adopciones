from appAdopciones.models.candidatos import Candidatos
from rest_framework import serializers

class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = ['Numero_Identificacion', 'Nombre_Completo', 'Direccion','Numero_Contacto','Email','Edad','Has_Tenido_Mascotas','Seras_Responsable','Tienes_Espacio','Tienes_Tiempo','Recursos_Economicos','Afrontar_Problemas','Resultado_Prueba']  
      
    '''def to_representation(self, obj):
        candi = Candidatos.objects.get(Id_Candidato = obj.Id_Candidato)
        return{
            'Nombrecito': candi.Nombre_Completo,
            'Edadcita': candi.Numero_Identificacion,
            'Disponibilidadcita': candi.Email

        }'''