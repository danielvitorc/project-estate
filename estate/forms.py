from django import forms
from .models import Acompanhamento

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['nome', 'numero', 'data', 'opcao', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
