from django.shortcuts import render, redirect
from .forms import UserForm

def cadastrar(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request,'cadastro.html',{"form":form})
