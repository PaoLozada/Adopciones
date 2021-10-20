"""appAdoptarMasscotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from appAdopciones.views import userCreateView
from appAdopciones.views.userDetailView import UserDetailView
from appAdopciones.views.userCreateView import UserCreateView
from appAdopciones.views.mascotaView import MascotaView
from appAdopciones.views.candidatosView import CandidatosView
from appAdopciones.views.solicitudView import SolicitudView
from django.urls import path
from django.views.generic.base import View
from rest_framework import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appAdopciones import views


urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('mascotas/', views.MascotaView.as_view()),
    path('candidatos/<int:pk>/', views.CandidatosDetail.as_view()),
    path('solicitud/', views.SolicitudView.as_view()),
    path('candidatos/', views.CandidatosView.as_view()),
    path('mascotas/<int:pk>/', views.MascotaDetail.as_view()),
    path('solicitud/<int:pk>/', views.SolicitudDetail.as_view()),
]
