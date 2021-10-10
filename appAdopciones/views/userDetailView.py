from django.conf import settings
import rest_framework
from rest_framework import serializers
from rest_framework.response import Response
from  rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from appAdopciones.models.user import User
from appAdopciones.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get ("HTTP,_AUTHORIZATION")[7:]
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT["ALGORITHM"])
        valid_data = tokenBackend.decode (token, verify = False)
        if valid_data ["user_id"]!=kwargs['pk']:
            stringResponse = {'detail': 'Unauthorize request'} 
            return Response (stringResponse, status = status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

        