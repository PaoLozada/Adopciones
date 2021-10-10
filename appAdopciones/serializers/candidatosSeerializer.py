from appAdopciones.models.candidatos import Candidatos
from rest_framework import serializers

class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = ['Numero_Identificacion', 'Nombre_Completo', 'Direccion','Numero_Contacto','Email','Edad','Resultado_Prueba']
        