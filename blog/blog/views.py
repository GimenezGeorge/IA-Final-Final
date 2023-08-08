from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'index.html')

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>P&aacute;gina No Encontrada</h1>')

def nosotros(request):
    return render(request, 'nosotros.html')