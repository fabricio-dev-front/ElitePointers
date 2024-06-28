from django.shortcuts import render, redirect
from Usuarios.models import Usuario
from Relogios.models import Relogio
from .models import Carrinho
from django.contrib.auth.decorators import login_required

@login_required
def adicionar_item(request,email,pk):
    usuario = Usuario.objects.get(email=email)
    carrinhos = usuario.carrinhos.all()
    relogio = Relogio.objects.get(id=pk)
    
    if relogio.quantidadeDisponivel > 0:
        
        if carrinhos is None:
            carrinhos = Carrinho()
            carrinhos.relogio = relogio
            carrinhos.quantidade = 1
            relogio.quantidadeDisponivel -= 1
            usuario.carrinho = carrinhos
            relogio.save()
            carrinhos.save()
            usuario.save()
            return redirect('home')

        for carrinho in carrinhos:
            if carrinho.relogio.id == pk:
                carrinho.quantidade += 1
                relogio.quantidadeDisponivel -= 1
                relogio.save()
                carrinho.save()
                return redirect('home')
        
        carrinhos = Carrinho()
        carrinhos.usuario = usuario
        relogio.quantidadeDisponivel -= 1
        carrinhos.relogio = relogio
        carrinhos.quantidade = 1
        relogio.save()
        carrinhos.save()
        return redirect('home')

@login_required
def remover_item(request,email,pk):
    usuario = Usuario.objects.get(email=email)
    carrinhos = usuario.carrinhos.all()

    for carrinho in carrinhos:
        if carrinho.relogio.id == pk:
            if carrinho.quantidade == 1:
                carrinho.delete()
                carrinhos.save()
                return redirect('home')
            else:
                carrinho.quantidade -= 1
                carrinho.save()
                return redirect('home')

@login_required
def listar_carrinhos(request,email):
    usuario = Usuario.objects.get(email=email)
    carrinhos = usuario.carrinhos.all()
    soma = 0
    for carrinho in carrinhos:
        soma += (carrinho.relogio.preco * carrinho.quantidade)

    return redirect('home',{"carrinhos":carrinhos,"precoTotal":soma})
    
