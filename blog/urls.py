from django.urls import path
from .views import HomePage, PreventView, DonationsView, about, post_detail_view

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('prevencao/', PreventView.as_view(), name="dicas"),
    path('doacoes/', DonationsView.as_view(), name="doacoes"),
    path('sobre/', about, name="sobre"),
    path('post/<int:pk>',post_detail_view, name="detalhar_post")
]
