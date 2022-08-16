from django.urls import path
from . import views

                                         #Escribir p/ ver vista en navegador: 
urlpatterns = [                          
    path('index/', views.index, name='index'), # http://127.0.0.1:8000/blog/index/
    path('time/', views.fecha_hora_actual, name='time'), # http://127.0.0.1:8000/blog/time/ 
    path('noticia_list.html', views.lista_noticias, name='noticia'), # (vista basada en funciones) http://127.0.0.1:8000/blog/noticia_list.html 
    path('listar/', views.ListaNoticia.as_view()), # (vista basada en clases) http://127.0.0.1:8000/blog/listar/  
]

