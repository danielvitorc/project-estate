from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_usuario, name='logout'),
    path('acompanhamento/', views.acompanhamento, name='acompanhamento'),
    path('acompanhamento/excluir/<int:pk>/', views.excluir_acompanhamento, name='excluir_acompanhamento'),
    path('logistica/', views.logistica, name='logistica'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
]