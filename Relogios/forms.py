from django.forms import ModelForm
from .models import Relogio

class RelogioForm(ModelForm):
    model = Relogio
    fields = "__all__"
