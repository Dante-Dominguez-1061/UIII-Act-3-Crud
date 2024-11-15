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
    precio = request.POST["numprecio"]
    fecha_lanzamiento = request.POST["txtfecha"]
    compañia = request.POST["txtcompañia"]
    stock = request.POST["numstock"]
    guardarconsola = Consola.objects.create(id_consola=id_consola,nombre=nombre,fabricante=fabricante,precio=precio,fecha_lanzamiento=fecha_lanzamiento,compañia=compañia,stock=stock)
    return redirect("/")

def seleccionarConsola(request,id_consola):
    consola = Consola.objects.get(id_consola=id_consola)
    return render(request,"editarConsola.html",{"misconsolas":consola})

def editarConsola(request):
    id_consola = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    fabricante = request.POST["txtfabricante"]
    precio = request.POST["numprecio"]
    fecha_lanzamiento = request.POST["txtfecha"]
    compañia = request.POST["txtcompañia"]
    stock = request.POST["numstock"]
    consola = Consola.objects.get(id_consola=id_consola)
    consola.nombre = nombre
    consola.fabricante = fabricante
    consola.precio = precio
    consola.fecha_lanzamiento = fecha_lanzamiento
    consola.compañia = compañia
    consola.stock = stock
    consola.save()
    return redirect("/")

def borrarConsola(request,id_consola):
    consola = Consola.objects.get(id_consola=id_consola)
    consola.delete()
    return redirect("/")