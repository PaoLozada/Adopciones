from appAdopciones.models.candidatos import Candidatos
from rest_framework import serializers

class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = ['Id_Candidato','Numero_Identificacion', 'Nombre_Completo', 'Direccion','Numero_Contacto','Email','Edad','Resultado_Prueba']  
      
    def to_representation(self, obj):
        candi = Candidatos.objects.get()
        return{
            'Nombrecito': candi.Nombre_Completo,
            'Edadcita': candi.Numero_Identificacion,
            'Disponibilidadcita': candi.Email

        }