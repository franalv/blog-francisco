from msilib.schema import Class
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from blog.forms import FormularioPosteos, Suscribirse, FormularioContacto
from blog.models import Busqueda, Suscriptores, Contacto, Posteos


def inicio(request):

    return render(request, "blog/index.html")

def publicacionesblog(request):

    return render(request, "blog/publicaciones.html")

def formularioposteos(request):

    if request.method == "POST":
        variable_1 = Posteos(request.POST)
        variable_1.save()
    return render(request, 'blog/formularioposteo.html')

class Contactarse(HttpRequest):

    def index(request):
        contacto = Contactarse()
        return render (request, "blog/formulariocontacto.html", {"form": contacto})
    
    def solicitudcontacto(request):
        contacto = Contactarse()
        if contacto.is_valid():
            contacto.save()
            contacto = Contactarse()
        
        return render (request, "blog/formulariocontacto.html", {"form": contacto, "mensaje": "OK"})

class Suscribirse(HttpRequest):

    def index(request):
        suscripcion = Suscribirse()
        return render(request, "blog/formulariosuscriptores.html", {"form": suscripcion})

    def registrosuscriptor(request):
        suscripcion = Suscribirse()
        if suscripcion.is_valid():
            suscripcion.save()
            suscripcion = Suscribirse()
        
        return render(request, "blog/formulariosuscriptores.html"), {"form": suscripcion, "mensaje": "Ok"}


def busqueda_publicaciones(request):

    return render(request, "blog/formulariobusqueda.html")

def buscador(request):

    if request.GET['bsc']:

        mensaje = "Buscaste la publicación %r" %request.GET['bsc']
        buscado = request.GET['bsc']

        buscado_2 = Busqueda.objects.filter(Texto__icontains=buscado)

        return render (request, "blog/resultado_busqueda.html", {"busqueda":buscado_2, "query":buscado})


    else:

        mensaje = "No introduciste ninguna búsqueda. Introducí algo para buscar"

    return HttpResponse(mensaje)

class FormularioPosteosView(HttpRequest):

    def index(request):
        publicacion = FormularioPosteos()
        return render (request, "blog/formularioposteo.html", {"form": publicacion})
    
    def procesar_formulario(request):
        publicacion = FormularioPosteos()
        if publicacion.is_valid():
            publicacion.save()
            publicacion = FormularioPosteos()
        
        return render(request, "blog/formularioposteo.html", {"form": publicacion, "mensaje": "OK"})