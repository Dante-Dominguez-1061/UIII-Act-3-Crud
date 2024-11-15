from django.urls import path
from Consola_app import views

urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarConsola/",views.registrarConsola,name="registrarConsola"),
    path("seleccionarConsola/<id_consola>",views.seleccionarConsola,name="seleccionarConsola"),
    path("editarConsola/",views.editarConsola,name="editarConsola"),
    path("borrarConsola/<id_consola>",views.borrarConsola,name="borrarConsola")
]
