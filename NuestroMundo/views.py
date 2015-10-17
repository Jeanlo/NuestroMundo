from django.shortcuts import render
from django.http import HttpResponse
from .models import Pais, Ciudad, Idioma_Pais, Idioma

def index(request):
    paises = Pais.objects.order_by('nombre')
    context = {'paises' : paises}
    return render(request, 'nuestromundo/index.html', context)
	
def pais(request, nombre_pais):
    pais = Pais.objects.get(codigo=nombre_pais)
    ciudades = Ciudad.objects.filter(codigo_pais=nombre_pais)
    capital = Ciudad.objects.get(pk=pais.capital)
    idiomas_pais = Idioma_Pais.objects.filter(codigo_pais=pais.codigo)
    context = {'pais' : pais, 'ciudades' : ciudades, 'capital' : capital, 'idiomas_pais' : idiomas_pais}
    return render(request, 'nuestromundo/pais.html', context)

def ciudad(request, id_ciudad):    
    ciudad = Ciudad.objects.get(pk=id_ciudad)
    pais = Pais.objects.get(codigo=ciudad.codigo_pais)
    context = {'ciudad' : ciudad, 'pais' : pais}
    return render(request, 'nuestromundo/ciudad.html', context)

def idioma(request, idioma_nombre):
    idioma = Idioma.objects.get(nombre=idioma_nombre)
    paises = Pais.objects.order_by('nombre')
    idioma_paises = Idioma_Pais.objects.filter(idioma=idioma.nombre)
    context = {'idioma' : idioma, 'idioma_paises' : idioma_paises, 'paises' : paises}
    return render(request, 'nuestromundo/idioma.html', context)