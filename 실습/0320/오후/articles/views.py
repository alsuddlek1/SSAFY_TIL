from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        # 특정 단어 드래그 후 ctrl + d : 같은 단어 다 찾아줌
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)