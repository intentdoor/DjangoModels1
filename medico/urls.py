from django.contrib import admin
from django.urls import path
from .views import listar_especialidades , cadastrar_especialidade , listar_medicos , cadastrar_medico

urlpatterns = [
    path('especialidades/', listar_especialidades, name='listar_especialidades'),
    path('especialidades/cadastrar/', cadastrar_especialidade, name='cadastrar_especialidade'),
    path('medicos/', listar_medicos, name='listar_medicos'),
    path('medicos/cadastrar/', cadastrar_medico, name='cadastrar_medico'),
]
