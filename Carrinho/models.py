from django.db import models
from Relogios.models import Relogio
from Usuarios.models import Usuario

class Carrinho(models.Model):
    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="carrinhos")
    relogio = models.ForeignKey(Relogio,on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.relogio}, Carrinho de {self.usuario}"
    

