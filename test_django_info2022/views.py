from django.http import HttpResponse
from django.template import loader 

import datetime

def saludo(request):
    now = datetime.datetime.now()
    template = loader.get_template("saludo.html")
    context={'hora': now}
    return HttpResponse(template.render(context, request)) 

def saludo2(request,horas):
    now = datetime.datetime.now()
    hora = now + datetime.timedelta(hours=horas)

    numero1 = float(input())
    numero2 = float(input())
    resultado = numero1 + numero2 

    template = loader.get_template("saludo2.html")
    context={'hora': now, 'adelantado':hora, 'n1':numero1, 'n2':numero2, 'r':resultado}

    return HttpResponse(template.render(context, request)) 