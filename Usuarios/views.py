from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login as login_django,logout as logout_django,authenticate
from custom_user.models import User
from .models import Usuario
from django.contrib.auth.decorators import login_required


def cadastrar(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            user = User.objects.create_user(first_name=nome,email=email,password=senha)
            if user:
                usuario = Usuario()
                usuario = form.save(commit=False)
                usuario.user = user
                usuario.save()
                return redirect('home')
    return render(request,'cadastro.html',{"form":form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request,email=email,password=senha)
        if user:
            login_django(request,user)
            return redirect('home')
        return redirect('login')
    
    return render(request,'login.html')

@login_required
def logout(request):
    logout_django(request)
    return redirect('home')

@login_required
def visualizar_usuario(request,email):
    usuario = User.objects.get(email=email)
    return render(request,'perfil.html',{"usuario": usuario})