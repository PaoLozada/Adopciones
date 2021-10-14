from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.models.mascotas import Mascotas
from appAdopciones.serializers.mascotaSerializer import MascotaSerializer

class MascotaView (views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = MascotaSerializer (data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

             


        '''tokenData = {"username": request.data["userData"], "pasword": request.data["pasword"]}
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''
        

    def get(self, request, *args, **kwargs):
        serializer = MascotaSerializer(Mascotas.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    