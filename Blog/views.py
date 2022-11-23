from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Categoria
import logging


# Create your views here.

def recetas(request):
    posts = Post.objects.all()
    return render(request, "Blog/categorias.html", {"posts": posts})


def categoria(request, categoria_id): 
    logging.debug(categoria_id)
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "Blog/categorias.html", {'categoria': categoria, 'posts': posts})

def receta(request, post_id):
    logging.debug(post_id)
    post = Post.objects.get(id=post_id)
    return render(request, "Blog/receta.html", {'post': post})



