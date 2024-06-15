from django.contrib import admin
from django.urls import path, include
from .views import home
from Usuarios import urls as urls_usuarios
from Relogios import urls as url_relogios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include(urls_usuarios)),
    path('relogios/',include(url_relogios))
]
