from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.serializers.solicitudSerializer import SolicitudSerializer
from appAdopciones.serializers.solicitudSerializer import SolicitudSerializer

class SolicitudView (views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = SolicitudSerializer (data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        '''tokenData = {"username": request.data["userData"], "pasword": request.data["pasword"]}
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''
        return Response(status=status.HTTP_201_CREATED)   