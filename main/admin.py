from django.contrib import admin
from .models import Profile, Article, Rating, SavedArticle

# Register your models here.

admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(SavedArticle)