from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Blog.models import Post

# Renderiza la pagina principal
def home(request):
    #obtiene las tres primeras recetas
    post  = Post.objects.all().order_by('created').reverse()[:6]
    print(post)
    return render(request, "Home/home.html", {'posts': post})