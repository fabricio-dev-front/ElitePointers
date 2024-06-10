from django.urls import path
from .views import cadastrar,login,logout

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastro'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]
