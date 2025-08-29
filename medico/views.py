from django.shortcuts import render
from forms import EspecialidadeForm , MedicoForm


def cadastrar_especialidade(request):
    form = EspecialidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_especialidades')
    return render(request, 'especialidades/cadastro.html', {'form': form})

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades/listar.html', {'especialidades': especialidades})


