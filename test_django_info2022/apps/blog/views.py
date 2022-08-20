from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Noticia
import datetime

# Create your views here.

# Vistas basadas en funciones

def index(request):
    '''Vista de prueba''' 
    return HttpResponse('<h1>Vista de prueba: blog</1>')

def fecha_hora_actual(request):
    '''Vista de prueba c/ contenido dinámico no de bd'''
    now = datetime.datetime.now()
    html = "<html><body><h1>Hoy es: %s.</h1></body></html>" % now
    return HttpResponse(html)

def lista_noticias(request):
    '''Vista de prueba c/ cont. dinam. de bd'''
    news = Noticia.objects.all()
    return render(request, 'noticia_list.html', {'news':news})

def vista_noticias(request): 
    noticias = Noticia.objects.all()
    return render(request, 'noticia_list.html', {'noticias':noticias})


# Vistas basadas en clases 

'''
class DetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticia_list.html'
'''
class ListaNoticia(ListView):
    model = Noticia
    template_name = 'noticia_list.html'


















