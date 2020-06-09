from rest_framework import serializers  
from main.models import Profile, Article, User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id', 'username','first_name','last_name','email', 'date_joined']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        exclude=['id',]
        model = Article