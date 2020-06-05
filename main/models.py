from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(null=True)
    phone = models.IntegerField(unique=True, null=True)
    photo = models.ImageField(upload_to='profiles')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

    @classmethod
    def save_profile(cls, user, bio, phone, photo):
        profile = cls(user=user, bio=bio, phone=phone, photo=photo)
        profile.save()
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
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user.id).first()
        return profile

    @classmethod
    def search_profile(cls, keywords):
        profiles = cls.objects.filter(Q(user__username__icontains=keywords)| Q(bio__icontains=keywords)).all()
        return profiles

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=255)
    description = models.TextField()
    publish = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    @classmethod
    def get_all_articles(cls):
        return cls.objects.exclude(publish=False).all()

    @classmethod
    def save_article(cls, user, title, link, description, publish):
        article = cls(user=user, title=title, link=link, description=description, publish=publish)
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
