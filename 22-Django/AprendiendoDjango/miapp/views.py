from django.shortcuts import render, HttpResponse

#MVC = Modelo vista controlador ->  Acciones(metodos)
#MVT = modelo vista template->      Acciones(Metodos)

def index(request):
    return HttpResponse("""
    <h1>Inicio</h1>
    """)


def hola_mundo(request):
    return HttpResponse("""
    <h1>Un Hola Mundo usando Django</h1>
    <h3>Alexander Correa Gutiérrez</h3>
    """)

def pagina(request):
    return HttpResponse("""
    <h1>Página Web</h1>
    <h3>Made by Alexander Correa Gutiérrez</h3>
    """)