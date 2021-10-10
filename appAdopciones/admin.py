from django.contrib import admin

from django.contrib import admin
from .models.user import User
from .models.mascotas import Mascotas
from .models.candidatos import Candidatos
from .models.solicitud import Solicitud


admin.site.register(User)
admin.site.register(Mascotas)
admin.site.register(Solicitud)
admin.site.register(Candidatos)
