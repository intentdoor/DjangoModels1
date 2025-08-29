from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('especialidades/', listar_especialidades, name='listar_especialidades'),
    path('especialidades/novo/', cadastrar_especialidade, name='cadastrar_especialidade'),
    path('medicos/', listar_medicos, name='listar_medicos'),
    path('medicos/novo/', cadastrar_medico, name='cadastrar_medico'),
]
