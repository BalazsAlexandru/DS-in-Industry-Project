from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'westTweets', views.TweetViewSet, basename='west-tweets')
router.register(r'russianTweets', views.RuTweetViewSet, basename='russian-tweets')
router.register(r'westSentiment', views.TweetSentimentViewSet, basename='west-sentiment')
router.register(r'russianSentiment', views.RuTweetSentimentViewSet, basename='russian-sentiment')

urlpatterns = [
    path('', views.index, name='index'),
    path('russian_tweets/', views.russianIndex, name='russian_tweets'),
    path('russian_tweets/russian_tweet_search/', views.ru_tweet_search, name='russian_tweets_search'),
    path('russian_tweets/russian_tweet_search_summarised/', views.ru_tweet_search_sumarised, name='russian_tweets_search_summarised'),
    path('russian_tweets/russian_sentiment/', views.ru_tweet_sentiment, name='russian_sentiment'),
    path('western_tweets/westIndex', views.westIndex, name='westIndex'),
    path('western_tweets/tweet_search/', views.tweet_search, name='tweet_search'),
    path('western_tweets/tweet_search_sumarised/', views.tweet_search_sumarised, name='tweet_search_summarised'),
    path('western_tweets/tweet_sentiment/', views.tweet_sentiment, name='tweet_sentiment'),
    path('sentimentPrediction/', views.sentimentPrediction, name='sentimentPrediction'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
