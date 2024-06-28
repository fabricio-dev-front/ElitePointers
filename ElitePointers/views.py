from django.shortcuts import render, redirect
from Relogios.models import Relogio

def home(request):
    relogios_masculinos = Relogio.objects.filter(genero='Masculino')[:10]
    relogios_femininos = Relogio.objects.filter(genero='Feminino')[:10]
    return render(request,'index.html',{'relogios_masculinos':relogios_masculinos, 'relogios_femininos':relogios_femininos})
