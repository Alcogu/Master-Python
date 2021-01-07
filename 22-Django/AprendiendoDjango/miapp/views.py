from django.shortcuts import render, HttpResponse, redirect

#MVC = Modelo vista controlador ->  Acciones(metodos)
#MVT = modelo vista template->      Acciones(Metodos)

layout = """
<h1>Sitio Web con Django | Alexander Correa Gutiérrez</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contactos</a>
    </li>
</ul>
<hr/>
"""

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """

    year = 2020
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)


def hola_mundo(request):
    return HttpResponse(layout+"""
    <h1>Un Hola Mundo usando Django</h1>
    <h3>Alexander Correa Gutiérrez</h3>
    """)

def pagina(request, redirigir = 0):

    if redirigir ==1:
        return redirect('/contacto/Alexander/Correa')
        #return redirect('/contacto', nombre="Alexander", apellidos="Correa Gutiérrez")

    return HttpResponse(layout+"""
    <h1>Página Web</h1>
    <h3>Made by Alexander Correa Gutiérrez</h3>
    """)

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)