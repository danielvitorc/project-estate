from django import forms
from .models import Acompanhamento, Estoque

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['nome', 'numero', 'data', 'opcao', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome', 'numero', 'data', 'opcao', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }