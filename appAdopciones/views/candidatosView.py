from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.models.candidatos import Candidatos
from appAdopciones.serializers.candidatosSeerializer import CandidatosSerializer

class CandidatosView (views.APIView):

    
    def get(self, request, format=None):
        candidato = Candidatos.objects.all()
        serializer = CandidatosSerializer(candidato, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CandidatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidatosDetail(views.APIView):
    
    

    def get(self, request, pk, format=None):
        candidato = self.get_object(pk)
        serializer = CandidatosSerializer(candidato)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        candidato = self.get_object(pk)
        serializer = CandidatosSerializer(candidato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidato = self.get_object(pk)
        candidato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)