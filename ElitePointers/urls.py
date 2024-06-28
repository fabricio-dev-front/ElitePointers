from django.contrib import admin
from django.urls import path, include
from .views import home
from Usuarios import urls as urls_usuarios
from Relogios import urls as url_relogios
from Carrinho import urls as url_carrinho
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include(urls_usuarios)),
    path('relogios/', include(url_relogios)),
    path('carrinho/', include(url_carrinho)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
