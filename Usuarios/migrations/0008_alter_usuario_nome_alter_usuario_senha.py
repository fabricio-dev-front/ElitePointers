# Generated by Django 5.0.6 on 2024-06-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0007_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
