from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from appbts.forms import * 

# Create your views here.

def inicio(request):
    return render (request, "appbts/inicio.html")

def bts(request):
    return render (request, "appbts/bts.html")

def coreasur(request):
    return render (request, "appbts/coreasur.html")

def army(request):
    return render (request, "appbts/army.html")

def btsFormulario(request): #formulario  API con Form de Django
    if request.method == "POST":
        form=BtsForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data 
            integrantes= informacion["integrantes"]
            bts= Bts (integrantes=integrantes)
            bts.save()
            return render(request, "appbts/inicio.html" , {"mensaje": "Integrante guardado correctamente"})
        else:
            return render(request, "appbts/btsFormulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= BtsForm()
        return render (request, "appbts/btsFormulario.html", {"form": formulario})



def coreaFormulario(request): #otro formulario

    if request.method == "POST":
        soft_power= request.POST["soft power"]
        corea1 = Coreasur(soft_power=soft_power)
        corea1.save()
        return render (request, "appbts/inicio.html", {"mensaje":"Contenido guardado correctamente"})
    else:
        return render (request, "appbts/coreaFormulario.html")

def armyFormulario(request):

    if request.method == "POST":
        resumen= request.POST["resumen"]
        army1 = Army(resumen=resumen)
        army1.save()
        return render (request, "appbts/inicio.html", {"mensaje":"Información guardada correctamente"})
    else:
        return render (request, "appbts/armyFormulario.html")


def busquedaBts(request):
    return render (request, "appbts/busquedaBts.html")

def buscar(request):
    integrantes=request.GET["integrantes"]
    if "integrantes"!="":
        integrantes=Bts.objects.filter(integrantes=integrantes)
        return render (request, "appbts/resultadoBusqueda.html", {"integrantes":integrantes})
    else:
        return render (request, "appbts/busquedaBts.html", {"mensaje": "Ingrese integrante" })