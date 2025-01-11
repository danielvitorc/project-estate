from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Acompanhamento, Estoque, Objeto
from .forms import AcompanhamentoForm, EstoqueForm, ObjetoForm
from django.shortcuts import get_object_or_404
import os

# ===== Tela de Login ===== 
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


# ===== Renderizar a tela Home se o login for bem sucedido =====
@login_required
def home(request):
    return render(request, 'estate/home.html')

# ===== Renderizar a tela Acompanhamento e função para cadastrar dados em um formulário =====
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


#  ===== Função que exclui dados do formulário da tela de Acompanhamentos ====
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


# ===== Renderiza a tela de Logistica se o login for bem sucedido ======
@login_required
def logistica(request):
    if request.method == 'POST':
        form_estoque = EstoqueForm(request.POST, request.FILES)
        if form_estoque.is_valid():
            form_estoque.save()
            return redirect('logistica')  # Redirecionar para evitar reenvio do formulário
    else:
        form_estoque = EstoqueForm()

    dados_estoque = Estoque.objects.all()  # Obter todos os registros
    return render(request, 'estate/logistica.html',{'form_estoque': form_estoque, 'dados_estoque': dados_estoque})

#  ===== Função que exclui dados do formulário da tela de Acompanhamentos ====
@login_required
def excluir_estoque(request, pk):
    dado_estoque = get_object_or_404(Estoque, pk=pk)
    # Verifica se a imagem existe e exclui do sistema de arquivos
    if dado_estoque.imagem:
        imagem_path_estoque = os.path.join(settings.MEDIA_ROOT, str(dado_estoque.imagem))
        if os.path.exists(imagem_path_estoque):
            os.remove(imagem_path_estoque)
    
    # Deleta o registro do banco de dados
    dado_estoque.delete()
    return redirect('logistica')  # Redireciona para a página de acompanhamento



# Função que verificar se o usuário é admin
def is_admin(user):
    return user.is_staff

# ===== Tela e função de cadastro de usuários com restrição para os administradores ======
@user_passes_test(is_admin)  # Apenas administradores podem acessar
def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Evitar duplicação de usuários
        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
        else:
            # Cria o novo usuário comum
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Usuário cadastrado com sucesso!")

        return redirect('cadastrar_usuario')

    return render(request, 'estate/cadastrar_usuario.html')


# ===== Tela e função de cadastro de Objetos com restrição para os administradores ======
@user_passes_test(is_admin)
def cadastrar_objeto(request):
    if request.method == 'POST':
        form_objeto = ObjetoForm(request.POST)
        if form_objeto.is_valid():
            form_objeto.save()
            
            return redirect('cadastrar_objeto')  # Redireciona para a lista de objetos após cadastro
    else:
        form_objeto = ObjetoForm()

    dados_objeto = Objeto.objects.all()  # Obter todos os registros
    return render(request, 'estate/cadastrar_objeto.html', {'form_objeto': form_objeto, 'dados_objeto': dados_objeto})

def excluir_objeto(request, id):
    dado_objeto = get_object_or_404(Objeto, id=id)
    dado_objeto.delete()
    return redirect('cadastrar_objeto')  # Redireciona para a página de cadastro após excluir

# ==== Função para deslogar do sistema =====
def logout_usuario(request):
    logout(request)
    return redirect('login')