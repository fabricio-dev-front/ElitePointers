from django.db import models
from django.utils.translation import gettext_lazy as _

class Relogio(models.Model):
    class Meta:
        verbose_name = 'Relógio'
        verbose_name_plural = 'Relógios'

    nome = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    marca = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to="Relogios/fotos")
    genero = models.CharField(
        max_length=9,
        choices = (
            ('Masculino','Masculino'),
            ('Feminino','Feminino'),
        ),
    )
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=20,blank=True,null=True)
    quantidadeDisponivel = models.IntegerField()
    peso = models.SmallIntegerField(
        choices=(
            (1, '1 kilate'),
            (10, '10 kilates'),
            (12, '12 kilates'),
            (14, '14 kilates'),
            (16, '16 kilates'),
            (18, '18 kilates'),
            (20, '20 kilates'),
            (22, '22 kilates'),
            (24, '24 kilates'),
        )
    )

    def __str__(self):
        return self.nome
