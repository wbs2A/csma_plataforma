from django.urls import path
from .views import _login, Register, update_profile, configurations, dashboard, ManageReports
urlpatterns = [
    path('acesso/', _login, name='login'),
    path('cadastro/', Register.as_view(), name='registrar'),
    path('painel/', dashboard, name='painel'),
    path('perfil/', update_profile, name='perfil'),
    path('configuracoes/', configurations, name='configuracao'),
    path('gerenciar-denuncias/', ManageReports.as_view(), name='gerenciar_denuncias'),

]
