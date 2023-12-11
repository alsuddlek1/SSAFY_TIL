from django.shortcuts import render
from .models import Music

# Create your views here.
def music_list(request):
    all_music = Music.objects.all()