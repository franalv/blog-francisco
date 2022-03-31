
from django.contrib import admin
from django.urls import path
from blog.views import FormularioPosteosView, inicio, publicacionesblog, Contactarse, Suscribirse, buscador, busqueda_publicaciones
from blog.models import Posteos, Suscriptores, Contacto, Busqueda

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('publicaciones/', publicacionesblog, name="Publicaciones"),
    path('suscribirse/', Suscribirse.index, name="Suscribirse"),
    path('enviosuscriptor/', Suscribirse.registrosuscriptor, name="RegistroSuscriptor"),
    path('contacto/', Contactarse.index, name="Contacto"),
    path('contacto/', Contactarse.solicitudcontacto, name="guardarcontacto"),
    path('buscar/', busqueda_publicaciones, name="BuscadorUno"),
    path('buscador/', buscador, name="Buscador"),
    path('crearpublicacion/', FormularioPosteosView.index, name="crearpublicacion"),
    path('guardarpublicacion/', FormularioPosteosView.procesar_formulario, name="guardarpublicacion"),
]
