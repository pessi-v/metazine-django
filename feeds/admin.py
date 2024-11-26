from django.contrib import admin
from .models import RSSFeed, FeedItem

@admin.register(RSSFeed)
class RSSFeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'last_fetched')
    search_fields = ('name', 'url')

@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'feed', 'published_date', 'og_image')
    list_filter = ('feed', 'published_date')
    search_fields = ('title', 'description', 'og_description')