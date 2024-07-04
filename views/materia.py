from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from computacion_api.serializers import *
from computacion_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json

class MateriaAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materias = Materia.objects.all().order_by("id")
        materia_data = MateriaSerializer(materias, many=True).data

        # Iterar sobre cada materia y cargar los datos de los días
        for materia in materia_data:
            materia["dias"] = json.loads(materia["dias"])

        return Response(materia_data, 200)

class MateriaView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materia, id = request.GET.get("id"))
        materia = MateriaSerializer(materia, many=False).data
        materia["dias"] = json.loads(materia["dias"])
        return Response(materia, 200)
    
    #Registrar nueva materia
    @transaction.atomic
    def post(self, request, *args, **kwargs):

            nombre = request.data["nombre"]
            existing_materia = Materia.objects.filter(nombre=nombre).first()

            if existing_materia:
                return Response({"message": f"El nombre de la materia '{nombre}' ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)
            #Para extraer de la base de datos hacer el json.load()
            #Create a profile for the user
            materia = Materia.objects.create(seccion= request.data["seccion"],
                                            salon= request.data["salon"],
                                            programa= request.data["programa"],
                                            nrc= request.data["nrc"],
                                            nombre= request.data["nombre"],
                                            horaInicio= request.data["horaInicio"],
                                            horaFinal= request.data["horaFinal"],
                                            dias = json.dumps(request.data["dias"]))
            materia.save()

            return Response({"materia_created_id": materia.id }, 201)

            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Se tiene que modificar la parte de edicion y eliminar
class MateriaViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        materia = get_object_or_404(Materia, id=request.data["id"])
        materia.nrc = request.data["nrc"]
        materia.seccion = request.data["seccion"]
        materia.nombre = request.data["nombre"]
        materia.horaInicio = request.data["horaInicio"]
        materia.horaFinal = request.data["horaFinal"]
        materia.dias = json.dumps(request.data["dias"])
        materia.salon = request.data["salon"]
        materia.programa = request.data["programa"]
        materia.save()
        user = MateriaSerializer(materia, many=False).data

        return Response(user,200)

    #Eliminar administrador
    def delete(self, request, *args, **kwargs):
        materia = get_object_or_404(Materia, id=request.GET.get("id"))
        try:
            materia.delete()
            return Response({"details":"Materia eliminada"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)