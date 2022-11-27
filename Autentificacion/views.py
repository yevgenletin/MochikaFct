from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login


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
                auth_login(request, usuario)
                return redirect("/Home/")
            else:
                for msg in form.error_messages:
                    print(msg)
                    messages.error(request, form.error_messages[msg])
                    return render(request, "Autentificacion/auth.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("/Home/")

def login(request):
    #Comprueba si los datos son correctos al hacer login
    if request.method == "POST":
        fr = AuthenticationForm(request, data = request.POST)
        if fr.is_valid():
            name = fr.cleaned_data.get("username")
            psw = fr.cleaned_data.get("password")
            user = authenticate(username=name, password=psw)
            if user is not None:
                auth_login(request, user)
                return redirect("/Home/")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Usuario y contraseña no coinciden")
            
    f=AuthenticationForm()
    return render(request,"Autentificacion/login.html",{"frm":f});