from django.shortcuts import render, HttpResponse

#MVC = Modelo vista controlador ->  Acciones(metodos)
#MVT = modelo vista template->      Acciones(Metodos)

def hola_mundo(request):
    return HttpResponse("Hola Mundo con Django")