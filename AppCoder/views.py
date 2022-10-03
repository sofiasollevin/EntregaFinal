from django.shortcuts import render
from AppCoder.models import jugadoresSelecciones, Contactos
from AppCoder.forms import ContactosFormulario, JugadoresFormulario

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


def nosotros(request):

      return render(request, "AppCoder/nosotros.html")

def error(request):
      from datetime import date
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
