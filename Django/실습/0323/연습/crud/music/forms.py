from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        modle = Music
        fields = '__all__'