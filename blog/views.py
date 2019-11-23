from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class HomePage(ListView):
    model = Post
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(categoria__exact="B").order_by('-published_date')

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


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={"post":post})


def about(request):
    staff = {"equipe": [
                            {"nome": "Wesley Barbosa", "img": "images/wesley.jpeg", "descript": "Programador python nas horas vagas e desenvolvedor deste site ^^", "class": "card-text text-white"},
                            {"nome": "Don Viton", "img": "images/kleber-bambam-instagram.jpg", "descript": "A acrescentar", "class":"card-text text-white"},
                            {"nome": "Gabriel MC", "img": "images/gabrielmc.jpg", "descript": "A acrescentar", "class":"card-text text-white"},
                            {"nome": "Helmuth Smiles", "img": "images/Helmuth.jpg",  "descript": "A acrescentar", "class": "card-text text-black"},
                            {"nome": "Valdenice da Silva", "img": "images/valdenize.jpg",  "descript": "A acrescentar", "class": "card-text text-white"}
                        ]
            }
    return render(request, 'blog/about.html', staff)

