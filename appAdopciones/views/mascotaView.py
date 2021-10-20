from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.models.mascotas import Mascotas
from appAdopciones.serializers.mascotaSerializer import MascotaSerializer

class MascotaView (views.APIView):
    def get(self, request, format=None):
        candidato = Mascotas.objects.all()
        serializer = MascotaSerializer(candidato, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaDetail(views.APIView):
    
    def get_object(self, pk):
        try:
            return Mascotas.objects.get(Id_Mascota=pk)
        except Mascotas.DoesNotExist:
            raise "Http404"

    def get(self, request, pk, format=None):
        mascota = self.get_object(pk)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        mascota = self.get_object(pk)
        serializer = MascotaSerializer(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)