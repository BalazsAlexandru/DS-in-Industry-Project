from django.core.management.base import BaseCommand

from ...models import Tweet


class Command(BaseCommand):
    help = 'Delete all rows from the TweetWithSentimentAnalysis table'

    def handle(self, *args, **options):
        Tweet.objects.all().delete()
