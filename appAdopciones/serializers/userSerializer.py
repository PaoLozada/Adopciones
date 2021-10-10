from appAdopciones.models.user import User
from rest_framework import serializers
from appAdopciones.models.solicitud import Solicitud
from appAdopciones.serializers.solicitudSerializer import SolicitudSerializer

class UserSerializer(serializers.ModelSerializer):
    solicitud = SolicitudSerializer
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email','solicitud']

    def create(self, validated_data):
        solicitudData = validated_data.pop ('solicitud')
        userInstance = User.objects.create(**validated_data)
        Solicitud.objects.create(user= userInstance, **solicitudData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        solicitud = Solicitud.objects.get(user= obj.id)
        
        return{
            'id': user.id,
            'username' : user.username,
            'password' : user.password,
            'name' : user.name,
            'email' : user.email,
            'solicitud':{
                'id_Solicitud' : solicitud.id_Solicitud,
                'id_User' : solicitud.id_User,
                'id_Mascotas' : solicitud.id_Mascotas,
                'id_Candidatos' : solicitud.id_Candidatos,
                'estado' : solicitud.estado,
                'respuesta' : solicitud.respuesta
            }
        }


        
       