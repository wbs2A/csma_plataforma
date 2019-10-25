from django.urls import path
from .views import homepage, CreateDenuncia

urlpatterns = [
    path('', homepage, name='denuncias'),
    path('novo', CreateDenuncia.as_view(), name='denuncias_create')

]
