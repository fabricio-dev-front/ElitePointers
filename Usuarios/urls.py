from django.urls import path
from .views import cadastrar,login,logout, visualizar_usuario

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastro'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('perfil/<str:email>/',visualizar_usuario,name='ver_usuario'),
]
