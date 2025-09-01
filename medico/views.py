from django.shortcuts import render , redirect
from .forms import EspecialidadeForm , MedicoForm 
from .models import Especialidade , Medico

def cadastrar_especialidade(request):
    form = EspecialidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_especialidades')
    return render(request, 'especialidades/cadastro.html', {'form': form})

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades/listar.html', {'especialidades': especialidades})


def cadastrar_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_medicos')
    return render(request, 'medicos/cadastro.html', {'form': form})


def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/listar.html', {'medicos': medicos})