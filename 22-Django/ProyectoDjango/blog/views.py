from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def list(request):

    #Sacar Articulos
    articles = Article.objects.all()#Saca todos los objetos

    #Paginar Articulos
    paginator = Paginator(articles, 2)

    #Recoger numero paginas
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html',{
        'title': 'Articulos',
        'articles': page_articles
    })

@login_required(login_url="login")
def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)#Saca todos los objetos
    #articles = Article.objects.filter(categories=category)

    return render(request, 'categories/category.html',{
        'category': category,
    })
    
@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        'article': article
    })