from rest_framework import serializers
from .models import WestTweet, RussianTweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WestTweet
        fields = ['tweet_id', 'tweet_created_at', 'tweet_text', 'tweet_user_name', 'tweet_retweets_count',
                  'tweet_likes_count', 'tweet_lang']


class TweetSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WestTweet
        fields = ['tweet_urls', 'tweet_date', 'tweet_sentiment']


class RuTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RussianTweet
        fields = ['ru_tweet_id', 'ru_tweet_created_at', 'ru_tweet_text', 'ru_tweet_user_name', 'ru_tweet_replies_count',
                  'ru_tweet_likes_count', 'ru_tweet_lang']


class RuTweetSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RussianTweet
        fields = ['ru_tweet_urls', 'ru_tweet_date', 'ru_tweet_sentiment']