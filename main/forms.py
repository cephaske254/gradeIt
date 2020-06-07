from .models import Article
from django import forms

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude=[]