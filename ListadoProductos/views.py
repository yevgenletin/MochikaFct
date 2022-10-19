
# Create your views here.
from django.views.generic.list import ListView
from django.shortcuts import render
import json
import datetime
from ListadoProductos.models import Listado
import logging

class InfoListView(ListView):
    model = Listado
    template_name = "ListadoProductos/lista.html"

    def get_context_data(self, **kwargs):
        def defaultconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()


        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Listado.objects.values()), default=defaultconverter)
        return context

def alimento(request, alimento_id):
    logging.debug(alimento_id)
    listado = Listado.objects.get(id = alimento_id)
    
    return render(request, "ListadoAlimentos/alimento.html", {'listado': listado})


