from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.
class HomePage(ListView):
    model = Post
    paginate_by = 3

def prevent(request):
    return HttpResponse("Prevenção e cuidados")

def donations(request):
    return HttpResponse("Gib money plis")

def about(request):
    return HttpResponse("Sobre nois")