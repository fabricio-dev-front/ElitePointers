# Generated by Django 5.0.6 on 2024-06-28 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrinho', '0002_alter_carrinho_relogio'),
        ('Usuarios', '0023_alter_usuario_options_remove_usuario_carrinho'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrinho',
            options={'verbose_name': 'Carrinho', 'verbose_name_plural': 'Carrinhos'},
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='Usuarios.usuario'),
        ),
    ]
