from django.urls import path
from .views import cadastrar, login, logout, visualizar, redireciona_admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', cadastrar, name='cadastro'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('alterarsenha/',auth_views.PasswordResetView.as_view(template_name='resetarSenha.html'),name='password_reset'),
    path('alterarsenhamensagem/',auth_views.PasswordResetDoneView.as_view(template_name='resetarsenhafeito.html'),name='password_reset_done'),
    path('confirmarsenha/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='resetarSenhaConfirmar.html'),name='password_reset_confirm'),
    path('alterarsenhaconcluido/',auth_views.PasswordResetCompleteView.as_view(template_name='resetarSenhaCompleto.html'),name='password_reset_complete'),
    path('perfil/<str:email>/',visualizar,name='ver_usuario'),
    path('redirecionar/',redireciona_admin,name='admin')
]
