from django.urls import path, include
from .import views
# urls below

urlpatterns=[
    path('users/', views.UsersView.as_view(), name='users_api'),
    path('users/<id>', views.UserView.as_view(), name='users_api'),
    path('articles/', views.ArticlesView.as_view(), name='articles_api'),
    path('articles/<id>', views.ArticleView.as_view(), name='article_api'),
]