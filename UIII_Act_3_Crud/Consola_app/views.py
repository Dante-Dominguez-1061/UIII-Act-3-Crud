from django.shortcuts import render,redirect
from .models import Consola
# Create your views here.

def inicio_vista(request):
    lasconsolas = Consola.objects.all()
    return render(request,"gestionarConsolas.html",{"misconsolas":lasconsolas})

def registrarConsola(request):
    id_consola = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    fabricante = request.POST["txtfabricante"]
    guardarconsola = Consola.objects.create(id_consola=id_consola,nombre=nombre,fabricante=fabricante)
    return redirect("/")

def seleccionarConsola(request,id_consola):
    consola = Consola.objects.get(id_consola=id_consola)
    return render(request,"editarConsola.html",{"misconsolas":consola})

def editarConsola(request):
    id_consola = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    fabricante = request.POST["txtfabricante"]
    consola = Consola.objects.get(id_consola=id_consola)
    consola.nombre = nombre
    consola.fabricante = fabricante
    consola.save()
    return redirect("/")

def borrarConsola(request,id_consola):
    consola = Consola.objects.get(id_consola=id_consola)
    consola.delete()
    return redirect("/")