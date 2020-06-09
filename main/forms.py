from .models import Article, Rating
from django import forms

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude=['user']

class ArticleRatingForm(forms.Form):
    usability = forms.CharField(widget=forms.NumberInput({'type':'range', 'max':10, 'value':'0', 'required':True, 'step':0.1}))
    design = forms.CharField(widget=forms.NumberInput({'type':'range', 'max':10, 'value':'0', 'required':True, 'step':0.1}))
    content = forms.CharField(widget=forms.NumberInput({'type':'range', 'max':10, 'value':'0', 'required':True, 'step':0.1}))
    article = forms.CharField(widget=forms.NumberInput({'type':'range',}))