from django.db import models

class Relogio(models.Model):
    nome = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    marca = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to="Relogios_fotos")
    genero = models.CharField(
        max_length=1,
        choices = (
            ('M','Masculino'),
            ('F','Feminino'),
        ),
    )
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=20,blank=True,null=True)
    peso = models.FloatField(
        max_length=4,
        blank=True,
        null=True,
        choices=(
            ('1','1'),
            ('10','10'),
            ('12','12'), 
            ('14','14'), 
            ('16','16'), 
            ('18','18'), 
            ('19.2','19.2'), 
            ('20','20'), 
            ('22','22'), 
            ('24','24'),
        )
    )

    def __str__(self):
        return self.nome
