from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


from ListadoProductos.models import Listado



# Create your views here.
def home(request):
    return render(request, "Home/home.html")

def recetas(request):
    return render(request, "Home/recetas.html")

def restaurantes(request):
    return render(request, "Home/restaurantes.html")
