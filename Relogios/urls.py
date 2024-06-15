from django.urls import path
from .views import cadastrarRelogio

urlpatterns = [
    path('criar/',cadastrarRelogio,name='cadastrarRelogio')
]