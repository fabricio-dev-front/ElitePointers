from django.urls import path
from .views import cadastrar, login, logout, visualizar, redireciona_admin

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastro'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('perfil/<str:email>/',visualizar,name='ver_usuario'),
    path('redirecionar/',redireciona_admin,name='admin')
]
