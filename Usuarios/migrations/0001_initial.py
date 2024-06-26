# Generated by Django 5.0.6 on 2024-05-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("sobrenome", models.CharField(max_length=50)),
                ("dataNascimento", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("permissao", models.BooleanField()),
            ],
        ),
    ]
