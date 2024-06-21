from django.db import models
from django.contrib.auth import get_user_model
from Relogios.models import Relogio
from django.utils.translation import gettext_lazy as _
from .validators import validate_cpf,validate_email,validate_name,validate_date

django_usuario = get_user_model()

class Carrinho(models.Model):

    relogio = models.ForeignKey(Relogio,on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Usuario(models.Model):
    user = models.OneToOneField(django_usuario,on_delete=models.CASCADE)
    nome = models.CharField(
        max_length=50,
        validators=[validate_name],
    )
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        error_messages={
            "unique": _("Já existe um usuário com esse email")
        }
    )
    cpf = models.CharField(
        max_length=14,
        validators=[validate_cpf],
        unique=True,
        error_messages={
            "unique": _("Já existe um usuário com esse cpf")
        }
    )
    dataNascimento = models.DateField(validators=[validate_date])
    senha = models.CharField(max_length=20)
    carrinho = models.ForeignKey(Carrinho,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nome
    
    

