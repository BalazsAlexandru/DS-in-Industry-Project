import csv
from django.core.management.base import BaseCommand
from ...models import WestTweet
from datetime import datetime


class Command(BaseCommand):
    help = 'Import tweets from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):

        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                id,tweet_id, created_at, date, time, username, name, tweet, language, mentions, photos, replies_count, retweets_count, likes_count, hashtags, link, retweet, video, reply_to, views_count,sentiment = row
                WestTweet.objects.create(
                    tweet_id=tweet_id,
                    tweet_created_at=created_at,
                    tweet_date=datetime.strptime(date, '%m/%d/%Y').date(),
                    tweet_time=time,
                    tweet_user_name=username,
                    tweet_name=name,
                    tweet_text=tweet,
                    tweet_lang=language,
                    tweet_mentions=mentions,
                    tweet_photos=photos,
                    tweet_replies_count=replies_count,
                    tweet_retweets_count=retweets_count,
                    tweet_likes_count=likes_count,
                    tweet_hashtags=hashtags,
                    tweet_urls=link,
                    tweet_retweet=retweet,
                    tweet_video=video,
                    tweet_reply_to=reply_to,
                    tweet_views_count=views_count,
                    tweet_sentiment=sentiment
                )
        self.stdout.write(self.style.SUCCESS('Tweets imported successfully'))
