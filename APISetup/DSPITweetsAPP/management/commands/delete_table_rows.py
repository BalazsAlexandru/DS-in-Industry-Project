from django.core.management.base import BaseCommand

from ...models import WestTweet


class Command(BaseCommand):
    help = 'Delete all rows from the WestTweets table'

    def handle(self, *args, **options):
        WestTweet.objects.all().delete()
