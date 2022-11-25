from django.shortcuts import render
from django.core.serializers import serialize

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Categoria
import logging
import json


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
    '''Estructura json ingredientes
    [
  {
    "nombre": "Pollo a la cerverza",
    "ingredientes": [
      {
        "pollo": "20gr"
      },
      {
        "cerveza": "20ml"
      },
      {
        "sal": "2gr"
      },
      {
        "pimienta": "30gr"
      },
      {
        "cebolla": "100gr"
      }
    ]
}
]
    '''
    try:
        logging.debug(post_id)
        post = Post.objects.get(id=post_id)
        jsn = json.loads(post.ingredientes)
        ingredientes = {}
       
        for j in jsn:
            print(j['nombre'])
            for i in j['ingredientes']:
                
                for key, value in i.items():
                    ingredientes[key] = value
                    print(ingredientes)        
        
        return render(request, "Blog/receta.html", {'post': post, 'ingredientes': ingredientes, 'jsn': jsn})
                
    except:
        print ("Receta introducida con errores")
        return render(request, "Blog/receta.html", {'post': post})

        
    
    



