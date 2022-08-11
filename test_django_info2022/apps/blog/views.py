from urllib import response
from django.shortcuts import render

from django.http import HttpResponse

from .models import Noticia


# Create your views here.

def index(request): 
    return HttpResponse('<h1>Vista de prueba: blog</1>') 

