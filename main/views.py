from django.shortcuts import render, HttpResponse
from .forms import NewArticleForm
from .models import Article
# Create your views here.
def home(request):
    articles = Article.get_all_articles()
    context = {
        'title':'Home | GradeIt',
        'articles':articles
    }
    return render(request,'home.html', context)

def new_article(request):
    form = NewArticleForm()
    user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            link = form.cleaned_data['link']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            Article.save_article(user,title, link,description, image,publish=True)
            

    context = {
        'title':'New Article | GradeIt',
        'form':form
    }
    return render(request,'new_article.html', context)
def profile(request, username):
    context={}
    return HttpResponse("hello")
