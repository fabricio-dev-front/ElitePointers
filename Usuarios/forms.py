from django.forms import ModelForm,TextInput,EmailInput,DateInput,PasswordInput
from .models import Usuario
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
class UserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome','email','cpf','dataNascimento','senha'
        ]
        widgets = {
            "nome": TextInput(attrs={"id":"nome","type":"text","placeholder":"Nome","name":"nome"}),
            "email": EmailInput(attrs={"id":"email","type":"email","placeholder":"seuemail@email.com","name":"email"}),
            "cpf": TextInput(attrs={"id":"cpf","type":"text","placeholder":"111.222.333-44","name":"cpf"}),
            "dataNascimento": TextInput(attrs={"id":"dataNascimento","type":"date","name":"data de nascimento"}),
            "senha": PasswordInput(attrs={"id":"senha","type":"password","placeholder":"Senha","name":"senha"})
        }
        labels = {
            "nome": "Nome:",
            "email": "Email:",
            "cpf": "cpf",
            "dataNascimento": "Data de nascimento:",
            "senha": "Senha:",
        }
        
        