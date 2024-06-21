import re
from django.core import validators
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import date


PADRAO_EMAIL = r'^[a-z0-9._]+@[a-z]+\.([a-z]{3,})(\.[a-z]{2,})?$'
PADRAO_CPF = r'^\d{3}.\d{3}.\d{3}-\d{2}$'
PADRAO_NOME = r'^([a-zA-Zá-úÁ-Ú]|\s)+$'

def validate_email(value):
    email = str(value)
    if not re.match(PADRAO_EMAIL,email):
        raise ValidationError('Padrão de email incorreto')
    
    
def validate_name(value):
    if not re.match(PADRAO_NOME,value):
        raise ValidationError('Nome inválido, digite apenas letras e espaços')
    
def validate_cpf(value):
    cpf = str(value)
    if not re.match(PADRAO_CPF,cpf):
        raise ValidationError('Padrão incorreto de cpf')
    
def validate_date(value):
    idade = relativedelta(date.today(),value).years
    if idade < 18:
        raise ValidationError('Voce não pode acessar o site, pois não é de maior')