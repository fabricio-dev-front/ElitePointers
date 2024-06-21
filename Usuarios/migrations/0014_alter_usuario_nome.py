# Generated by Django 5.0.6 on 2024-06-18 01:40

import Usuarios.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0013_usuario_datanascimento_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50, validators=[Usuarios.validators.validate_name]),
        ),
    ]
