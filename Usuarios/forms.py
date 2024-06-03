from django.forms import ModelForm,TextInput,EmailInput,DateInput
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'nome','sobrenome','dataNascimento','email'
        ]
        widgets = {
            "nome": TextInput(attrs={"id":"nome","type":"text","placeholder":"Nome"}),
            "sobrenome": TextInput(attrs={"id":"sobrenome","type":"text","placeholder":"Sobrenome"}),
            "dataNascimento": DateInput(attrs={"id":"dataNascimento","type":"date"}),
            "email": EmailInput(attrs={"id":"email","type":"email","placeholder":"Email"}),
        }
        labels = {
            "nome": "Nome:",
            "sobrenome": "Sobrenome:",
            "dataNascimento": "Data de nascimento:",
            "email": "Email:",
        }
        