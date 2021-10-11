from appAdopciones.models.solicitud import Solicitud
from rest_framework import serializers

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id_User','id_Mascotas','id_Candidatos','estado', 'respuesta']
        