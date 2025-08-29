from django import forms
from .models import Especialidade
from .models import Medico

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade      
        fields = ['nome']        

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico      
        fields = ['nome']