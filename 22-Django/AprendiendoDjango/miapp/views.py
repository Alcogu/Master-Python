from django.shortcuts import render,HttpResponse

#MVC = Modelo vista controlador -> Acciones(metodos)
#MVT = modelo vista template-> Acciones(Metodos)

def holaMundo(request):
    return HttpResponse("Hola Mundo con Django")