from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk) #조회한거 가져오기
    context = {'article' : article} 
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')