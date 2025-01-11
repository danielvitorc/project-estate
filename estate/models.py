from django.db import models


class Objeto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nome
    

class Acompanhamento(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    data = models.DateField()
    opcao = models.CharField(max_length=50, choices=[
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
    ])
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE, default=1)
    imagem = models.ImageField(upload_to='uploads/acompanhamento')

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    data = models.DateField()
    opcao = models.CharField(max_length=50, choices=[
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
    ])
    imagem = models.ImageField(upload_to='uploads/estoque')

    def __str__(self):
        return self.nome
    


    
