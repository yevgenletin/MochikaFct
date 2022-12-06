from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Post


from ListadoProductos.models import Listado



# Create your views here.
def home(request):
    post  = Post.objects.all().order_by('created').reverse()[:6]
    print(post)
    return render(request, "Home/home.html", {'posts': post})

def recetas(request):
    return render(request, "Home/recetas.html")

def restaurantes(request):
    return render(request, "Home/restaurantes.html")
