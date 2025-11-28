from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo (request):
    return HttpResponse ("inicio prueba2")
def pagina1 (request):
    return render(request, "index.html")
def pagina2 (request):
    return render(request, "indexpagina2.html")
