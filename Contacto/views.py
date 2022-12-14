from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Contacto.form import Formulario
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import re 
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# Recibe los datos del formulario contaco
# Comprueba los datos si son validos y envia el email

def contacto(request):
    formulario_contacto = Formulario()

    if request.method == "POST":

        if (formulario_contacto.is_valid):
            if(re.search(regex,request.POST.get("email"))):  
                print("Valid Email")
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
                email.send()
                return redirect("/Contacto/?valido")
            else:  
                 print("Invalid Email") 
                 return redirect("/Contacto/?novalido")

    return render(request, "Contacto/contacto.html", {'miFormulario': formulario_contacto})
    