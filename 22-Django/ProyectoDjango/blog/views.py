from django.shortcuts import render
from blog.models import Category, Article

def list(request):

    articles = Article.objects.all()#Saca todos los objetos

    return render(request, 'articles/list.html',{
        'title': 'Articulos',
        'articles': articles
    })