from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    email = models.EmailField()
    permissao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
