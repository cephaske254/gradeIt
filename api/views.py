from django.shortcuts import render
from rest_framework import response, views, status, authentication, permissions
from main.models import Article, Rating, User
from .serializers import UserSerializer, ArticleSerializer
# Create your views here.


class ArticlesView(views.APIView):
    def get(self, request, format=None):
        permission_classes = [permissions.AllowAny]
        data = Article.get_all_articles()
        serializers = ArticleSerializer(data, many=True)
        return response.Response(serializers.data, status=status.HTTP_200_OK)

class ArticleView(views.APIView):
    def get(self, request, id, format=None):
        rating = Rating.get_article_ratings(Article.get_article(id))
        data = Article.get_article(id)
        serializers = ArticleSerializer(data, many=False)
        return response.Response(serializers.data, status=status.HTTP_200_OK)

class UsersView(views.APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return response.Response(serializers.data, status=status.HTTP_200_OK)


class UserView(views.APIView):
    def get(self, request, id, format=None):
        users = User.objects.get(pk=id)
        serializers = UserSerializer(users, many=False)
        return response.Response(serializers.data, status=status.HTTP_200_OK)