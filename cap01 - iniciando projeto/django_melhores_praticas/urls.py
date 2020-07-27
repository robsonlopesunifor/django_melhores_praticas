"""
Configuração de URL django_melhores_praticas

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações, consulte:
     https://docs.djangoproject.com/en/2.2/topics/http/urls/
Exemplos:
Vistas de funções
     1. Adicione uma importação: das visualizações de importação do my_app
     2. Adicione um URL a urlpatterns: path ('', views.home, name = 'home')
Visualizações baseadas em classe
     1. Adicione uma importação: from other_app.views import Home
     2. Adicione um URL aos urlpatterns: path ('', Home.as_view (), name = 'home')
Incluindo outro URLconf
     1. Importe a função include (): de django.urls import include, path
     2. Adicione um URL a urlpatterns: path ('blog /', include ('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_a/', include('app_a.urls')),
]
