from django.urls import path
from .views import cadastrar

urlpatterns = [
    path('criar/',cadastrar,name='cadastrarRelogio')
]