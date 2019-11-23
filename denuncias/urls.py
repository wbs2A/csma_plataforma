from django.urls import path
from .views import homepage, contatos, CreateDenuncia, relatorios, sucesso

urlpatterns = [
    path('', homepage, name='denuncias'),
    path('novo/', CreateDenuncia.as_view(), name='denuncias_create'),
    path('contatos/', contatos, name='contatos'),
    path('estatisticas/', relatorios, name="estatisticas"),
    path('sucesso/', sucesso, name="success"),
]
