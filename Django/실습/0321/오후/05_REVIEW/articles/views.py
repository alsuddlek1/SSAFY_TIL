from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

# GET /articles/create : 게시글 생성 페이지 조회
# 게시글 생성을 위해 DB에 저장
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)