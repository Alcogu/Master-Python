from django.shortcuts import render

def list(request):

    return render(request, 'articles/list.html',{
        'title': 'Articulos'
    })