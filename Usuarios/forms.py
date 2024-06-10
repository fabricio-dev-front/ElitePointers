from django.forms import ModelForm,TextInput,EmailInput,DateInput,PasswordInput
from .models import Usuario
class UserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome','sobrenome','email','senha'
        ]
        widgets = {
            "nome": TextInput(attrs={"id":"nome","type":"text","placeholder":"Nome","name":"nome"}),
            "sobrenome": TextInput(attrs={"id":"sobrenome","type":"text","placeholder":"Sobrenome","name":"sobrenome"}),
            "email": EmailInput(attrs={"id":"email","type":"email","placeholder":"Email","name":"email"}),
            "senha": PasswordInput(attrs={"id":"senha","type":"password","placeholder":"Senha","name":"senha"})
        }
        labels = {
            "nome": "Nome:",
            "sobrenome": "Sobrenome:",
            "email": "Email:",
            "senha": "Senha:",
        }
        