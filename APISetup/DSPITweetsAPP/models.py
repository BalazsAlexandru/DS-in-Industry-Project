from django.db import models


# Create your models here.
class WestTweet(models.Model):
    tweet_id = models.DecimalField(max_digits=25, decimal_places=0)
    tweet_created_at = models.CharField(max_length=100)
    tweet_date = models.DateField()
    tweet_time = models.TimeField()
    tweet_user_name = models.CharField(max_length=100)
    tweet_name = models.CharField(max_length=100)
    tweet_text = models.CharField(max_length=1000)
    tweet_lang = models.CharField(max_length=100)
    tweet_mentions = models.CharField(max_length=100)
    tweet_photos = models.CharField(max_length=100)
    tweet_replies_count = models.IntegerField()
    tweet_retweets_count = models.IntegerField()
    tweet_likes_count = models.IntegerField()
    tweet_hashtags = models.CharField(max_length=100)
    tweet_urls = models.CharField(max_length=100)
    tweet_retweet = models.CharField(max_length=100)
    tweet_video = models.CharField(max_length=100)
    tweet_reply_to = models.CharField(max_length=100)
    tweet_views_count = models.IntegerField()
    tweet_sentiment = models.FloatField()

    def __str__(self):
        return self.tweet_text


# Create your models here.
class RussianTweet(models.Model):
    ru_tweet_id = models.DecimalField(max_digits=25, decimal_places=0)
    ru_tweet_created_at = models.CharField(max_length=100)
    ru_tweet_date = models.DateField()
    ru_tweet_time = models.TimeField()
    ru_tweet_user_name = models.CharField(max_length=100)
    ru_tweet_name = models.CharField(max_length=100)
    ru_tweet_text = models.CharField(max_length=1000)
    ru_tweet_lang = models.CharField(max_length=100)
    ru_tweet_mentions = models.CharField(max_length=100)
    ru_tweet_photos = models.CharField(max_length=100)
    ru_tweet_replies_count = models.IntegerField()
    ru_tweet_retweets_count = models.IntegerField()
    ru_tweet_likes_count = models.IntegerField()
    ru_tweet_hashtags = models.CharField(max_length=100)
    ru_tweet_urls = models.CharField(max_length=100)
    ru_tweet_retweet = models.CharField(max_length=100)
    ru_tweet_video = models.CharField(max_length=100)
    ru_tweet_reply_to = models.CharField(max_length=100)
    ru_tweet_views_count = models.IntegerField()
    ru_tweet_sentiment = models.FloatField()

    def __str__(self):
        return self.ru_tweet_text


