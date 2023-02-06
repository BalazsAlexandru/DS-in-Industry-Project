import csv
from django.core.management.base import BaseCommand
from ...models import RussianTweet
from datetime import datetime


class Command(BaseCommand):
    help = 'Import tweets from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):

        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                id, tweet_id, created_at, date, time, username, name, tweet, language, mentions, photos, replies_count, retweets_count, likes_count, hashtags, link, retweet, video, reply_to, views_count,sentiment = row
                RussianTweet.objects.create(
                    ru_tweet_id=tweet_id,
                    ru_tweet_created_at=created_at,
                    ru_tweet_date=datetime.strptime(date, '%m/%d/%Y').date(),
                    ru_tweet_time=time,
                    ru_tweet_user_name=username,
                    ru_tweet_name=name,
                    ru_tweet_text=tweet,
                    ru_tweet_lang=language,
                    ru_tweet_mentions=mentions,
                    ru_tweet_photos=photos,
                    ru_tweet_replies_count=replies_count,
                    ru_tweet_retweets_count=retweets_count,
                    ru_tweet_likes_count=likes_count,
                    ru_tweet_hashtags=hashtags,
                    ru_tweet_urls=link,
                    ru_tweet_retweet=retweet,
                    ru_tweet_video=video,
                    ru_tweet_reply_to=reply_to,
                    ru_tweet_views_count=views_count,
                    ru_tweet_sentiment=sentiment
                )
        self.stdout.write(self.style.SUCCESS('Tweets imported successfully'))
