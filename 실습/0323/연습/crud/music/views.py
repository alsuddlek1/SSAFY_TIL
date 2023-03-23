from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm

# Create your views here.
def index(request):
    music = Music.objects.all()
    context = {'music' : music}
    return render(request, 'music/index.html')

def detail(request, pk):
    musicc = Music.object.get(pk=pk)
    context = {'musicc':musicc}
    return render(request, 'music/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.Files)
        if form.is_valid():
            article = form.save()
            # return redirect('music:')
    else:
        form = MusicForm()
    context = {'form' : form}
    return render(request, 'music/create.html', context)