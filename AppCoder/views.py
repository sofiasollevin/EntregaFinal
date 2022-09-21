from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import jugadoresSelecciones, Contactos, Suscripciones, Usuarios
from AppCoder.forms import ContactosFormulario, JugadoresFormulario, NosotrosFormulario, SuscripcionesFormulario, UsuariosForm

# Create your views here.

def inicio(request):

      return render(request, "AppCoder/home.html")

def selecciones(request):

      jugador = []

      if request.method == "POST":
            pais= request.POST.get('pais')
            jugador= jugadoresSelecciones.objects.filter(pais__icontains=pais)

      contexto = {
            'my_form': jugadoresSelecciones(),
            'jugadores': jugador
      }

      return render(request, "AppCoder/selecciones.html", contexto)

def noticias(request):

      return render(request, "AppCoder/blogNoticias.html")

def noticia1(request):

      return render(request, "AppCoder/noticia1.html")

def contactosFormulario(request):

      if request.method == "POST":
            
            miFormularioContactos= ContactosFormulario(request.POST)
            print(miFormularioContactos)

            if miFormularioContactos.is_valid:
                  
                  informacion = miFormularioContactos.cleaned_data
                  contactos = Contactos(email=informacion['email'], nombre=informacion['nombre'], contactotelefonico=informacion['contactotelefonico'], mensaje=informacion['mensaje'])
                  contactos.save()
                  return render(request, "AppCoder/home.html")

      else:
            miFormularioContactos= ContactosFormulario()
      return render(request, "AppCoder/contact.html",{"miFormulario":miFormularioContactos})


def suscripcionesFormulario(request):
      if request.method == "POST":

            miFormularioSuscripciones = SuscripcionesFormulario(request.POST)
            print(miFormularioSuscripciones)

            if miFormularioSuscripciones.is_valid:
                  informacion = miFormularioSuscripciones.cleaned_data
                  suscripciones = Suscripciones(email=informacion['email'])
                  suscripciones.save()
                  return render(request, "AppCoder/home.html")

      else:
            miFormularioSuscripciones = SuscripcionesFormulario()
      return render(request, "AppCoder/padre.html", {"miFormulario": miFormularioSuscripciones})


def usuarioFormulario(request):
      if request.method == "POST":

            miFormularioUsuarios = UsuariosForm(request.POST)
            print(miFormularioUsuarios)

            if miFormularioUsuarios.is_valid:
                  informacion = miFormularioUsuarios.cleaned_data
                  usuarios = Usuarios(usuario=informacion['usuario'], nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], contrasena=informacion['contrasena'])
                  usuarios.save()
                  return render(request, "AppCoder/home.html")

      else:
            miFormularioUsuarios = UsuariosForm()
      return render(request, "AppCoder/login.html", {"miFormulario": miFormularioUsuarios})

def nosotros(request):

      return render(request, "AppCoder/nosotros.html")

def error(request):
      from datetime import date, datetime
      fecha_actual = date.today()
      diccionario = {"fecha": fecha_actual}
      return render(request, "AppCoder/error.html", diccionario)

def jugadoresForm(request):

      if request.method == "POST":
            
            miFormularioJugadores= JugadoresFormulario(request.POST)
            print(miFormularioJugadores)

            if miFormularioJugadores.is_valid:
                  
                  informacion = miFormularioJugadores.cleaned_data
                  jugadores = jugadoresSelecciones(pais=informacion['pais'], nombre=informacion['nombre'], apellido=informacion['apellido'], nacimiento=informacion['nacimiento'], posicion=informacion['posicion'])
                  jugadores.save()
                  return render(request, "AppCoder/selecciones.html")
      else:
            miFormularioJugadores= JugadoresFormulario()
      return render(request, "AppCoder/jugadoresFormulario.html",{"miFormulario":miFormularioJugadores})

def nosotrosFormulario(request):
      if request.method == "POST":

            miFormularioNosotros= NosotrosFormulario(request.POST)
            print(miFormularioNosotros)

            if miFormularioNosotros.is_valid:

                  informacion = miFormularioNosotros.cleaned_data
                  nosotros = Nosotros(nombre=informacion['nombre'], apellido=informacion['apellido'], numerofuncionario=informacion['numerofuncionario'], contactotelefonico=informacion['contactotelefonico'], email=informacion['email'])
                  nosotros.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormularioNosotros= NosotrosFormulario()
      return render (request, "AppCoder/nosotrosFormulario.html",{"miFormulario":miFormularioNosotros})
      
      
  