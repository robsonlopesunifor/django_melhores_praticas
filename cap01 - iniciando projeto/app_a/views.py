from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagina_inicial_view(request):
    return HttpResponse('Ola mundo')