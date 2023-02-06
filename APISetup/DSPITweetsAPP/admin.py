from django.contrib import admin

# Register your models here.

from .models import WestTweet
from .models import RussianTweet


admin.site.register(WestTweet)
admin.site.register(RussianTweet)