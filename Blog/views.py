from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Categoria, Comment
from .form import MessageForm
import logging
import json


# Create your views here.

def recetas(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
   
    return render(request, "Blog/categorias.html", {"posts": posts, "categorias": categorias})


def categoria(request, categoria_id): 
    logging.debug(categoria_id)
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "Blog/categorias.html", {'categoria': categoria, 'posts': posts, 'categorias': categorias})

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
        comments = Comment.objects.all()
        jsn = json.loads(post.ingredientes)
        ingredientes = {}
        print(comments)
        for j in jsn:
            print(j['nombre'])
            for i in j['ingredientes']:
                
                for key, value in i.items():
                    ingredientes[key] = value
                    print(ingredientes)        
        
        return render(request, "Blog/receta.html", {'post': post, 'ingredientes': ingredientes, 'jsn': jsn,  "form": MessageForm})
                
    except:
        print ("Receta introducida con errores")
        return render(request, "Blog/receta.html", {'post': post})

def comentario(request, post_id):
  member = Comment(post_id = post_id, name = request.user.username, body = request.POST.get('body'))
  member.save()
  return redirect('/Blog/receta/'+ str(post_id)+'/')
    



