from django.shortcuts import render
from django.http import HttpResponse
from .models import estudiante

# Create your views here.

def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    print(estudiantes)
    return render(request, "estudiantes/index.html")

def crear(request):
    return render(request, "estudiantes/crear.html")

def editar(request):
    return render(request, "estudiantes/editar.html")


