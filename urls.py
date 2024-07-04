"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from computacion_api.views import bootstrap
from computacion_api.views import admin
from computacion_api.views import alumnos
from computacion_api.views import maestros
from computacion_api.views import auth
from computacion_api.views import materia


urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', admin.AdminView.as_view()),
    #Admin Data
        path('lista-admin/', admin.AdminAll.as_view()),
    #Edit Admin
        path('admins-edit/', admin.AdminsViewEdit.as_view()),
    #Create Alumno
        path('alumnoss/', alumnos.AlumnoView.as_view()),
    #Alumno Data
        path('lista-alumno/', alumnos.AlumnosAll.as_view()),
    #Alumno Data
        path('alumnos-edit/', alumnos.AlumnosViewEdit.as_view()),
    #Create maestro
        path('maestro/', maestros.MaestrosView.as_view()),
    #Maestro Data
        path('lista-maestro/', maestros.MaestrosAll.as_view()),
    #Edit Maestro
        path('maestros-edit/', maestros.MaestrosViewEdit.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view()),
    #Crear Materia
        path('materia/', materia.MateriaView.as_view()),
    #Listar Materias       
        path('lista-materia/', materia.MateriaAll.as_view()),
    #Edit Materia
        path('materia-edit/', materia.MateriaViewEdit.as_view()),
]
 