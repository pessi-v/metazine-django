import feedparser
from celery import shared_task
from django.utils import timezone
from .models import RSSFeed, FeedItem

@shared_task
def fetch_rss_feeds():
    feeds = RSSFeed.objects.all()
    for feed in feeds:
        parsed_feed = feedparser.parse(feed.url)
        
        for entry in parsed_feed.entries:
            # Prevent duplicate entries
            unique_id = entry.get('id', entry.link)
            existing_item = FeedItem.objects.filter(unique_id=unique_id).first()
            
            if not existing_item:
                FeedItem.objects.create(
                    feed=feed,
                    title=entry.title,
                    link=entry.link,
                    description=entry.get('summary', ''),
                    published_date=timezone.now(),
                    unique_id=unique_id
                )
        
        feed.last_fetched = timezone.now()
        feed.save()