from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


##def autentificacion(request):
##    return render (request, "Autentificacion/auth.html")

class Vregistro(View):
        def get(self, request):
            form = UserCreationForm()
            return render(request, "Autentificacion/auth.html", {"form": form})
            

        def post(self, request):
            form=UserCreationForm(request.POST)
            if form.is_valid():
                usuario=form.save()
                login(request, usuario)
                return redirect("/Home/")
            else:
                pass
