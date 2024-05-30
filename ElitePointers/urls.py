from django.contrib import admin
from django.urls import path, include
from .views import home
from Usuarios import urls as urls_usuarios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include(urls_usuarios)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
