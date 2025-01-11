from django import forms
from .models import Acompanhamento, Estoque, Objeto


class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do objeto'}),
        }

class AcompanhamentoForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = ['nome', 'numero', 'data', 'opcao', 'imagem', 'objeto']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        objeto = forms.ModelChoiceField(queryset=Objeto.objects.all(), empty_label="Escolha um Objeto")

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nome', 'numero', 'data', 'opcao', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }


        