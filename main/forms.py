from .models import Article, Rating
from django import forms

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude=['user']

class ArticleRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = []