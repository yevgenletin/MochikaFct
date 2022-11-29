
# Create your views here.
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
import json
import datetime
from ListadoProductos.models import Listado
from Favoritos.models import Favoritos


class InfoListView(ListView):
    model = Listado
    template_name = "ListadoProductos/lista.html/"

    def get_context_data(self, **kwargs):
        def defaultconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()


        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Listado.objects.values()), default=defaultconverter)
        return context

def alimento(request, alimento_id):
    
    listado = Listado.objects.get(id = alimento_id)
    ##if(request.user):
    favoritos = Favoritos.objects.filter(id_user= request.user.id, id_producto = alimento_id).first()
    img = Listado.objects.filter(id = alimento_id)
    if(favoritos):
        print ("tiene")
        print(listado)
    else:
        print("no tiiene")
    

    ##for f in favoritos:
        ##print(f.id_producto)
        ##if(f.id_producto == alimento)
    ##else:
        ##favoritos = False
    
    print(img)
    
    return render(request, "ListadoProductos/alimento.html/", {'listado': listado, 'favoritos': favoritos, 'img': img})

#def delete(request, id):
    
    #try:
        #member = Favoritos.objects.get(id_producto=id)
        #member.delete()
        #return redirect('alimento', id)
        
    #except Favoritos.DoesNotExist:
        #comment = None
        #return redirect('alimento', id)

def addrecord(request, id, name):
  member = Favoritos(id_producto=id, id_user=request.user.id, name = name)
  member.save()
