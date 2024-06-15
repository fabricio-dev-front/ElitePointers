from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RelogioForm
from .models import Relogio

def cadastrarRelogio(request):
    form = RelogioForm()
    if request.method == "POST":
        if form.is_valid:
            form.save()
    
    return render(request,'cadastroRelogio.html',{'form': form})

def listRelogios(request):
    relogios_masculinos = Relogio.objects.get(genero='M')
    relogios_femininos = Relogio.objects.get(genero='F')
    return redirect('home',{'relogios_masculino':relogios_masculinos},{'relogios_femininos':relogios_femininos})

