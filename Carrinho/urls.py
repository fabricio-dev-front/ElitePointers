from django.urls import path, include
from .views import adicionar_item, remover_item, listar_carrinhos

urlpatterns = [
    # path('adicionarAoCarrinho/<str:email>/<int:pk>/<int:quantidade>/',adiciona_ao_carrinho,name="Adicionar_ao_carrinho"),
    path('adicionarUmAoCarrinho/<str:email>/<int:pk>/',adicionar_item,name="Adicionar_item_carrinho"),
    path('removerDoCarrinho/<str:email>/<int:pk>/',remover_item,name="remover_item_carrinho"),
    path('listarCarrinho/<str:email>/',listar_carrinhos,name="listar_carrinhos")
]
