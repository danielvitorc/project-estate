from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Acompanhamento
from .forms import AcompanhamentoForm
from django.shortcuts import get_object_or_404
import os

@login_required
def home(request):
    return render(request, 'estate/home.html')

@login_required
def acompanhamento(request):
    if request.method == 'POST':
        form = AcompanhamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('acompanhamento')  # Redirecionar para evitar reenvio do formulário
    else:
        form = AcompanhamentoForm()

    dados = Acompanhamento.objects.all()  # Obter todos os registros
    return render(request, 'estate/acompanhamento.html', {'form': form, 'dados': dados})



@login_required
def excluir_acompanhamento(request, pk):
    dado = get_object_or_404(Acompanhamento, pk=pk)
    # Verifica se a imagem existe e exclui do sistema de arquivos
    if dado.imagem:
        imagem_path = os.path.join(settings.MEDIA_ROOT, str(dado.imagem))
        if os.path.exists(imagem_path):
            os.remove(imagem_path)
    
    # Deleta o registro do banco de dados
    dado.delete()
    return redirect('acompanhamento')  # Redireciona para a página de acompanhamento

@login_required
def logistica(request):
    return render(request, 'estate/logistica.html')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial pós-login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'estate/login.html')


def logout_usuario(request):
    logout(request)
    return redirect('login')
