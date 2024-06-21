from django.shortcuts import render, redirect
from .forms import RelogioForm
from .models import Relogio
from Usuarios.models import Usuario,Carrinho
from django.db.models import Q

def cadastrar(request):
    form = RelogioForm()
    if request.method == "POST":
        if form.is_valid:
            form.save()
    
    return render(request,'cadastroRelogio.html',{'form': form})

def listar(request):
    relogios_masculinos = Relogio.objects.get(genero='M')
    relogios_femininos = Relogio.objects.get(genero='F')
    return redirect('home',{'relogios_masculino':relogios_masculinos},{'relogios_femininos':relogios_femininos})

def filtrar(request,busca):
    relogios = Relogio.objects.filter(
        Q(nome__contains=busca) | Q(cor__contains=busca) | Q(marca__contains=busca) | Q(material__contains=busca)
    )
    return redirect('page',{'relogios':relogios})

def adiciona_no_carrinho(request,email,pk,quantidade):
    carrinho = Usuario.objects.get(email=email).carrinho
    relogio = Relogio.objects.get(id=pk)
    quantidade_disponivel = relogio.quantidadeDisponivel
    if quantidade_disponivel >= quantidade:
        carrinho = Carrinho()
        carrinho.relogio = relogio
        carrinho.quantidade = quantidade
        carrinho.save()
        relogio.quantidadeDisponivel = quantidade_disponivel - quantidade
        relogio.save()

    return redirect('home')



