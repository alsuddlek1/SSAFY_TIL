from django import forms
from .models import Article

class ArticleForm(forms.ModelsForm):
    class Meta:
        model = Article
        fields = '__all__'
