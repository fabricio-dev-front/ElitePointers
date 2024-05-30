from django.db import models

class Relogio(models.Model):
    nome = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    marca = models.CharField(max_length=30)
    imagem = models.ImageField()
    genero = models.CharField(max_length=1)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
