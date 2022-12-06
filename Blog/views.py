from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.http import JsonResponse

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Categoria, Comment
from .form import MessageForm
import logging
import json



# Create your views here.
class RecetasView(ListView):
  model = Post
  paginate_by = 6
  context_object_name = "posts"
  template_name = 'Blog/categorias.html'
  ordering = ['name']
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RecetasView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        context['categorias'] = Categoria.objects.all()
        return context

class CategoriaView(ListView):
  model = Categoria
  context_object_name = "categorias"
  template_name = 'Blog/categorias.html'
 
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
        total_comments = Comment.objects.filter(post_id = post_id).count()
        
        comments = Comment.objects.filter(post_id = post_id)[0:5]
        print(total_comments)
        print(comments)

        jsn = json.loads(post.ingredientes)
        ingredientes = {}
        for j in jsn:
            print(j['nombre'])
            for i in j['ingredientes']:
                
                for key, value in i.items():
                    ingredientes[key] = value
                    print(ingredientes)        
        
        return render(request, "Blog/receta.html", {
          'post': post, 
          'ingredientes': ingredientes, 
          'jsn': jsn,  
          'form': MessageForm,
          'total_comments': total_comments,
          'comments': comments
          });
                
    except:
        print ("Receta introducida con errores")
        return render(request, "Blog/receta.html", {'post': post})

def comentario(request, post_id):
  member = Comment(post_id = post_id, name = request.user.username, body = request.POST.get('body'))
  member.save()
  return redirect('/Blog/receta/'+ str(post_id)+'/')

def loadMore(request):
  
  post_id = request.GET.get('post_id')
  total_item = int(request.GET.get('total_item'))
  limit = 5
  post_obj = Comment.objects.filter(post_id = post_id).values()
  print(total_item)
  queryset = Comment.objects.filter(post_id = post_id).values()[total_item : total_item + limit  ]
  return JsonResponse({"data": list(queryset)})
  


    



