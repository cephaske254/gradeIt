from django.shortcuts import render
from .forms import NewArticleForm
# Create your views here.
def home(request):
    context = {
        'title':'Home | GradeIt'
    }
    return render(request,'home.html', context)

def new_article(request):
    form = NewArticleForm()
    context = {
        'title':'New Article | GradeIt',
        'form':form
    }
    return render(request,'new_article.html', context)
