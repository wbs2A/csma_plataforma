from django.urls import path
from .views import HomePage, prevent, donations, about

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('prevencao/', prevent, name="dicas"),
    path('doacoes/', donations, name="doacoes"),
    path('sobre/', about, name="sobre"),

]
