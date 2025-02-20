from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name

# Modelo para crear los alumnos
class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_alumno = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return "Perfil del alumno "+self.first_name+" "+self.last_name


# Modelo para crear Maestros
class Maestro(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_maestro = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255, null=True, blank=True)
    cubiculo = models.CharField(max_length=255, null=True, blank=True)
    area_investigacion = models.CharField(max_length=255,null=True, blank=True)
    materias = models.CharField(max_length=255,null=True, blank=True)


    def __str__(self):
        return "Perfil del alumno "+self.first_name+" "+self.last_name

# Modelo para crear Materias
class Materia(models.Model):
    id = models.BigAutoField(primary_key= True)
    nrc = models.CharField(max_length=255, null=True, blank=True) 
    seccion = models.CharField(max_length=255, null=True, blank=True) 
    nombre = models.CharField(max_length=255, null=True, blank=True) 
    horaInicio = models.CharField(max_length=255, null=True, blank=True) 
    horaFinal = models.CharField(max_length=255, null=True, blank=True) 
    dias = models.CharField(max_length=255, null=True, blank=True) 
    salon = models.CharField(max_length=255, null=True, blank=True) 
    programa = models.CharField(max_length=255, null=True, blank=True) 
    