from django.shortcuts import render
from django.views.generic import CreateView
from .models import Denuncia
# Create your views here.
def homepage(request):
    return render(request, 'denuncias/homepage.html')


class CreateDenuncia(CreateView):
    model = Denuncia
    fields = ['latitude', 'longitude', 'observacao', 'conhece_origem', 'contato']