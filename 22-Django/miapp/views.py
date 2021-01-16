from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

#MVC = Modelo vista controlador ->  Acciones(metodos)
#MVT = modelo vista template->      Acciones(Metodos)
layout = """

"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    ""

    year = 2020
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    """
    year =2021
    hasta = range(year, 2051)


    nombre='Alexander Correa Gutiérrez'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

    if redirigir ==1:
        return redirect('/contacto/Alexander/Correa')
        #return redirect('/contacto', nombre="Alexander", apellidos="Correa Gutiérrez")

    return render(request, 'pagina.html')

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content} ")

def articulo(request):

    try:
        articulo = Article.objects.get(id=6, public=True)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: <strong>{articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all()
    #articulos = Article.objects.order_by('id')
    #articulos = Article.objects.order_by('-id')#Muestra lista invertida
    #articulos = Article.objects.order_by('-id')[:3]#Muestra primeros 3
    #articulos = Article.objects.order_by('-id')[2:5]#Muestra del 2 al 5

    return render(request, 'articulos.html',{
        'articulos': articulos #pasa objetos de la BD al template
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')