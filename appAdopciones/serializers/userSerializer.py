from appAdopciones.models.user import User
from rest_framework import serializers
from appAdopciones.models.solicitud import Solicitud


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email']

    '''def create(self, validated_data):
        solicitudData = validated_data.pop ('solicitud')
        userInstance = User.objects.create(**validated_data)
        Solicitud.objects.create(user= userInstance, **solicitudData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        
        
        return{
            'username' : user.username,
            'password' : user.password,
            'name' : user.name,
            'email' : user.email
            
        }'''
        