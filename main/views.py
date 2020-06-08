from django.shortcuts import render, HttpResponse, redirect
from .forms import NewArticleForm, ArticleRatingForm
from .models import Article, Rating
# Create your views here.
def home(request):
    articles = Article.get_all_articles()
    rating_form = ArticleRatingForm()
    if request.method == 'POST':
        rating_form = ArticleRatingForm(request.POST)
        if rating_form.is_valid():
            article = Article.get_article(rating_form.cleaned_data['article'])
            design = rating_form.cleaned_data['design']
            usability = rating_form.cleaned_data['usability']
            content = rating_form.cleaned_data['content']
            Rating.save_rating(request.user,article, design,usability,content)
            if (request.META['HTTP_REFERER']):
                return redirect(request.META['HTTP_REFERER'])
            return redirect('home')

    context = {
        'title':'Home | GradeIt',
        'articles':articles,
        'rating_form':rating_form
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

def single_article(request, id):
    article = Article.get_article(id)
    context = {
        'article':article
    }
    return render(request,'single_article.html', context)


def profile(request, username):
    context={}
    return HttpResponse("hello")
