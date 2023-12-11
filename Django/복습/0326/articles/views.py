from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm

# Create your views here.
def index(request):
    articles = Music.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Music.objects.get(pk = pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music = form.save()
            return redirect('articles:detail', music.pk)
    else:
        form = MusicForm()
    context = {'form' : form}
    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Music.objects.get(pk=pk)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk = article.pk)
    else:
        form = MusicForm(instance=article)
    context = {'form' : form, 'article' : article}
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Music.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')