from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Post


class HomePage(ListView):
    model = Post
    paginate_by = 3
    def get_queryset(self):
        return Post.objects.filter(categoria__exact="B")

class PreventView(ListView):
    model = Post
    template_name = 'blog/prevencao_list.html'
    context_object_name = 'prevent_post_list'

    def get_queryset(self):
        return Post.objects.filter(categoria__exact="P")


class DonationsView(ListView):
    model = Post
    template_name = 'blog/doacoes_list.html'
    context_object_name = 'donate_post_list'

    def get_queryset(self):
        return Post.objects.filter(categoria__exact="Do")


def about(request):
    staff = {"equipe": [
                            {"nome": "Wesley Barbosa"},
                            {"nome": "Don Viton"},
                            {"nome": "Gabriel MC"},
                            {"nome": "Helmuth Smiles"},
                            {"nome": "Valdenice da Silva"}
                        ]
            }
    return render(request, 'blog/about.html', staff)

