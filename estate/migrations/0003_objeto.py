# Generated by Django 5.1.4 on 2025-01-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_estoque_alter_acompanhamento_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
