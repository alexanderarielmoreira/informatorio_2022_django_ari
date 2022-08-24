"""test_django_info2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from test_django_info2022 import views

from test_django_info2022.settings import base
from test_django_info2022.static import static 
 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('blog/', include('test_django_info2022.apps.blog.urls')), # Incluye todas las urls de 'blog'
    path('hora/', views.saludo, name="hora"), # url estática
    path('hora2/<int:horas>', views.saludo2, name="hora2"), # url dinámica (se le pasa un parámetro)
    path('vista/', views.vista_test, name="vista_noticia"),
] + static(base.STATIC_URL, document_root=base.MEDIA_ROOT) 

