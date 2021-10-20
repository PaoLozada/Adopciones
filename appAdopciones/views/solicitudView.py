from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.models.solicitud import Solicitud 
from appAdopciones.serializers.solicitudSerializer import SolicitudSerializer

class SolicitudView (views.APIView):
    def get(self, request, format=None):
        candidato = Solicitud.objects.all()
        serializer = SolicitudSerializer(candidato, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitudDetail(views.APIView):
    
    def get_object(self, pk):
        try:
            return Solicitud.objects.get(id_Solicitud=pk)
        except Solicitud.DoesNotExist:
            raise "Http404"

    def get(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)