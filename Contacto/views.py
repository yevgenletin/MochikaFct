from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Contacto.form import Formulario
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def contacto(request):
   
    formulario_contacto = Formulario()

    if request.method == "POST":

        if (formulario_contacto.is_valid):
            formulario_contacto = Formulario(data=request.POST) 
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage(
                "Mensaje desde Web Mochika",
                "El usuario con nombre {} con la direccion {} escribe: \n\n {}".format(name, email, content),
                "",
                ["yevgen.letin@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect("/Contacto/?valido")
            except:
                return redirect("/Contacto/?novalido")

    return render(request, "Contacto/contacto.html", {'miFormulario': formulario_contacto})
    