from rest_framework import status, views
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appAdopciones.models.candidatos import Candidatos
from appAdopciones.serializers.candidatosSeerializer import CandidatosSerializer

class CandidatosView (views.APIView):
    def post (self, request, *args, **kwargs):
        serializer = CandidatosSerializer (data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        '''tokenData = {"username": request.data["userData"], "pasword": request.data["pasword"]}
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''
        return Response(status=status.HTTP_201_CREATED)

    '''def get(self, request, Id_Candidato, format=None):
        candidato = self.get_object(Id_Candidato)
        serializer = CandidatosSerializer(candidato)
        return Response(serializer.data)'''
    def get_object(self, pk):
        try:
            return Candidatos.objects.get(Id_Candidatos=pk)
        except Candidatos.DoesNotExist:
            raise ("Http404")


    def get(self, request, *args, **kwargs):
        serializer = CandidatosSerializer(Candidatos.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        candidato = self.get_object(pk)
        serializer = CandidatosSerializer(candidato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, Id_Candidato, format=None):
        candidato = self.get_object(Id_Candidato)
        candidato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    