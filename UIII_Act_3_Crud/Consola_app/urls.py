from django.urls import path
from Consola_app import views

urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista")
]
