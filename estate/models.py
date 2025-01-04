from django.db import models

class Acompanhamento(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    data = models.DateField()
    opcao = models.CharField(max_length=50, choices=[
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
    ])
    imagem = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nome
