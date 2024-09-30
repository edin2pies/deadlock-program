# recommender/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item_recommender/', views.item_recommender, name='item_recommender'),
    path('hero_stats/', views.hero_stats, name='hero_stats'),
]
