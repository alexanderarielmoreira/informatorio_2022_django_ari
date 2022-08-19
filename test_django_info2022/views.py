from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import datetime

from test_django_info2022.apps.blog.models import Noticia 

def saludo(request):
    now = datetime.datetime.now()
    template = loader.get_template("saludo.html")
    context={'hora': now}
    return HttpResponse(template.render(context, request)) 

def saludo2(request,horas):
    now = datetime.datetime.now()
    hora = now + datetime.timedelta(hours=horas)

    #Toda esta lógica corre y se ejecuta desde el CMD, no el template... 
    #Pero funcionó muy bien y sirvió la prueba!!!
    numero1 = float(input())
    numero2 = float(input())
    resultado = numero1 + numero2 

    #Esta variable extrae datos del modelo. Esta bien pero le falta
    #un trozo de código para obtener los valores registrados. 
    fechaPublicacion = Noticia.published_date

    #template = loader.get_template("saludo2.html")
    context={'hora': now, 'adelantado':hora, 'n1':numero1, 'n2':numero2, 'r':resultado, 'fecha_public':fechaPublicacion}

    #return HttpResponse(template.render(context, request)) S/render 
    return render(request, 'saludo2.html', context) # c/ render 

