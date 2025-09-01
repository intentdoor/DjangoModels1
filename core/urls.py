"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from medico.views import listar_especialidades , cadastrar_especialidade , listar_medicos , cadastrar_medico


urlpatterns = [
    path('admin/', admin.site.urls),
    path('especialidades/', listar_especialidades, name='listar_especialidades'),
    path('medicos/', listar_medicos, name='listar_medicos'),
    path('medicos/cadastrar/', cadastrar_medico, name='cadastrar_medico'),
    path('especialidades/cadastrar/', cadastrar_especialidade, name='cadastrar_especialidade'),
]


