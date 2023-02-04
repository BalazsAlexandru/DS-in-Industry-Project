from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet_search/', views.tweet_search, name='tweet_search'),
    path('tweet_search_sumarised/', views.tweet_search_sumarised, name='tweet_search_summarised'),
    path('tweet_sentiment/', views.tweet_sentiment, name='tweet_sentiment'),
]
