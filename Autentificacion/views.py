from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


##def autentificacion(request):
##    return render (request, "Autentificacion/auth.html")

##Renderiza la hoja de registro de usuario.
class Vregistro(View):
        def get(self, request):
            form = UserCreationForm()
            return render(request, "Autentificacion/auth.html", {"form": form})
            
## Comprobacion del usuario y contraseña.
        def post(self, request):
            form=UserCreationForm(request.POST)
            if form.is_valid():
                usuario=form.save()
                login(request, usuario)
                return redirect("/Home/")
            else:
                for msg in form.error_messages:
                    print(msg)
                    messages.error(request, form.error_messages[msg])
                    return render(request, "Autentificacion/auth.html", {"form": form})
                
