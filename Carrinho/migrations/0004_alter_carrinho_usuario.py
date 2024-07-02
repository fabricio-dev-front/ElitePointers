# Generated by Django 5.0.6 on 2024-06-28 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrinho', '0003_alter_carrinho_options_carrinho_usuario'),
        ('Usuarios', '0023_alter_usuario_options_remove_usuario_carrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='Usuarios.usuario'),
        ),
    ]