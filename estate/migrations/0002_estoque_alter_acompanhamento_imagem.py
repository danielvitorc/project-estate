# Generated by Django 5.1.4 on 2025-01-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=15)),
                ('data', models.DateField()),
                ('opcao', models.CharField(choices=[('opcao1', 'Opção 1'), ('opcao2', 'Opção 2'), ('opcao3', 'Opção 3')], max_length=50)),
                ('imagem', models.ImageField(upload_to='uploads/estoque')),
            ],
        ),
        migrations.AlterField(
            model_name='acompanhamento',
            name='imagem',
            field=models.ImageField(upload_to='uploads/acompanhamento'),
        ),
    ]
