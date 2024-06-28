from django.shortcuts import render, redirect
from .forms import RelogioForm
from .models import Relogio
from django.db.models import Q

def cadastrar(request):
    form = RelogioForm()
    if request.method == "POST":
        if form.is_valid:
            form.save()
    
    return render(request,'cadastroRelogio.html',{'form': form})

def filtrar(request,busca):
    relogios = Relogio.objects.filter(
        Q(nome__contains=busca) | Q(cor__contains=busca) | Q(marca__contains=busca) | Q(material__contains=busca)
    )
    return redirect('page',{'relogios':relogios})



