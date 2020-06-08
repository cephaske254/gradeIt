from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_article/', views.new_article, name='new_article'),
    path('<username>/', views.profile, name='profile'),

]