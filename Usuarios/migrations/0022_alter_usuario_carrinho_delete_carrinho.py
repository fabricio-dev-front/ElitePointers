# Generated by Django 5.0.6 on 2024-06-23 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrinho', '0001_initial'),
        ('Usuarios', '0021_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='carrinho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Carrinho.carrinho'),
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
    ]
