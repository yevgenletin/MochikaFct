from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Favoritos
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

'''
  Renderiza los datos de la tabla Favoritos
'''
def favoritos(request):
  mydata = Favoritos.objects.filter(id_user = request.user.id).values()

  context = {
    'favoritos': mydata,
  }
  return render(request, "Favoritos/favoritos_list.html/", context)

'''
  Crea el alimento en la tabla Favoritos
  Solo pueden acceder usuarios registrados
  Recibe peticion ajax desde alimento.html
  devuelve json del alimento
'''
class CreateFavoritos(View):
   def  get(self, request):
    if request.user.is_authenticated:
      id_producto = request.GET.get('id_producto', None)
      name = request.GET.get('name', None)
      valor = request.GET.get('valor', None)
      comment = request.GET.get('comment', None)
      favoritos = Favoritos.objects.filter(id_user= request.user.id, id_producto = id_producto)
      if favoritos:
          pass
      else:
        obj = Favoritos.objects.create(
            id_user = User.objects.get(id = request.user.id),
            id_producto = id_producto,
            name = name,
            valor = valor,
            comment = comment
        )
      favoritos = {'id_producto':obj.id_producto,'name':obj.name,'comment':obj.comment}
      data = {
            'favoritos': favoritos
      }
      return JsonResponse(data)

'''
  Actualiza el alimento de la tabla Favoitos
  Solo pueden acceder usuarios registrados
  Recibe peticion ajax desde alimento.html
  devuelve json del alimento
'''
class UpdateFavoritos(View):

   def  get(self, request):
    print(request.user.id)
    if request.user.is_authenticated:
      
      id_producto = request.GET.get('id_producto', None)
      valor = request.GET.get('valor', None)
      comment = request.GET.get('comment', None)

      favoritos = Favoritos.objects.filter(id_user= request.user.id, id_producto = id_producto).update(valor=valor, comment=comment)  

      data = {
            'favoritos': favoritos
      }
      return JsonResponse(data)

##Elimina items de la tabla  favoritos
class DeleteFavoritos(View):
  def  get(self, request, id):
     
    if request.user.is_authenticated:
      print("Eliminado" + str(id))
      try:
        favoritos = Favoritos.objects.filter(id_user= request.user.id, id_producto = id).last()
        event = Favoritos.objects.get(id_user= request.user.id, id_producto=id)
        event.delete()
        ## Envia mensaje si elimina el objeto
        messages.success(request, 'eliminado   '+ str(favoritos.name) )
        return redirect('/Favoritos/')
      except:
        ## manda mensaje de error si no puede eliminarse
        messages.error(request, ' no se ha podido eliminar   '+ str(favoritos.name) )
        return redirect('/Favoritos/')
        
