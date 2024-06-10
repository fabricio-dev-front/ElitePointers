from django.db import models
from django.contrib.auth import get_user_model

django_usuario = get_user_model()

class Usuario(models.Model):
    
    user = models.OneToOneField(django_usuario,on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
