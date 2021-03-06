from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import statistics
from django.http import JsonResponse
from django.core import serializers
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(null=True)
    phone = models.IntegerField(unique=True, null=True)
    photo = models.ImageField(upload_to='profiles',null=False)
    country = CountryField(blank_label='select country', null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @classmethod
    def save_profile(cls, user, bio, phone,country, photo):
        profile = cls(user=user, bio=bio, phone=phone, photo=photo, country=country)
        profile.save()
        return profile

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user.id).first()
        return profile

    @classmethod
    def update_profile(cls, user, bio, phone, photo):
        profile = cls.get_profile(user)
        profile.bio = bio or profile.bio
        profile.phone = phone or profile.phone
        profile.photo = photo or profile.photo
        profile.save()
        return profile


    @classmethod
    def search_profile(cls, keywords):
        profiles = cls.objects.filter(Q(user__username__icontains=keywords)| Q(bio__icontains=keywords)).all()
        return profiles

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles')
    description = models.TextField()
    publish = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def article_data(self):
        data = (serializers.serialize('json', [self]).strip('[]'))
        return data

    
    def __str__(self):
        return self.title
    @property
    def design_grade(self):
        ratings = Rating.get_article_rating_by_field(self, 'design')
        return round(statistics.mean(ratings),1)
        
    @property
    def usability_grade(self):
        ratings = Rating.get_article_rating_by_field(self, 'usability')
        return round(statistics.mean(ratings),1)

    @property
    def content_grade(self):
        ratings = Rating.get_article_rating_by_field(self, 'content')
        return round(statistics.mean(ratings),1)
    @property
    def average_grade(self):
        average = statistics.mean([self.content_grade, self.usability_grade, self.design_grade])
        return round(average, 1)

    @classmethod
    def get_all_articles(cls):
        return cls.objects.exclude(publish=False).all()

    @classmethod
    def save_article(cls, user, title, link, description,image, publish):
        article = cls(user=user, title=title, link=link, description=description, image=image, publish=publish)
        article.save()
        return article

    @classmethod
    def update_article(cls,id, title, link, description, publish):
        article = cls.get_article(id)
        article.title = title or article.title
        article.link = title or article.link
        article.description = description or article.description
        article.publish = publish or article.publish
        article.save()
        return article

    @classmethod
    def get_article(cls, id):
        article = cls.objects.get(pk=id)
        return article

    @classmethod
    def search_articles(cls, keywords):
        articles = cls.objects.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords) | Q(link__icontains=keywords), publish=True)
        return articles

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='rating')
    design = models.FloatField(default=0)
    usability = models.FloatField(default=0 )
    content = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} rated {self.article.user.username}\'s article - {self.article.description}'
    @property
    def average(self):
        return round(statistics.mean([self.content,self.usability,self.design]), 1)
        

    @classmethod
    def save_rating(cls, user, article, design, usability, content):
        rating = cls(user=user, article=article, design=design, usability=usability, content=content)
        rating.save()
        print(user)
        return rating

    @classmethod
    def get_article_ratings(cls, article):
        return cls.objects.filter(article=article.id).all()
    @classmethod
    def get_article_rating_by_field(cls, article, field):
        item_list = []
        items = cls.objects.filter(article=article.id).values_list(field, flat=True).all()
        if not items : items=[0]
        for item_ in items :
            item_list.append(item_)
        return item_list

    @classmethod
    def get_ratings_by_user(cls, user):
        ratings = cls.objects.filter(user=user.id).all()
        return ratings

    @classmethod
    def get_rating(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def update_rating(cls, id, design, usability, content):
        rating = cls.get_rating(id)
        rating.design = design or rating.design
        rating.usability = usability or rating.usability
        rating.content = content or rating.content
        rating.save()
        return rating

class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_aricles')
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

    @classmethod
    def get_collections(cls, user):
        list_ = []
        saved = cls.objects.filter(user=user.id).all()
        for one in saved:
            list_.append(one.article)
        return list_
    @classmethod
    def save_unsave_article(cls, user, article):
        try:
            cls.objects.filter(user=user.id, article=article.id).first().delete()
            return 'Removed from collection refresh needed to effect changes'
        except:
            cls(user=user, article=article).save()
            return 'Added to collection refresh needed to effect changes'

