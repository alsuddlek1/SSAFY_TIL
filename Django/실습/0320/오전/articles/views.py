from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context= {'article' : article}
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 새로운 Article 저장
    # Article.objects.create(
    #     title=title,
    #     content=content
    # )

    article = Article(title=title, content=content)
    article.save()

    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete
    return redirect('articles:index')