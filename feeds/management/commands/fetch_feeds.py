from django.core.management.base import BaseCommand
from feeds.tasks import fetch_rss_feeds

class Command(BaseCommand):
    help = 'Fetches all RSS feeds immediately'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting RSS feed fetch...')
        fetch_rss_feeds()
        self.stdout.write(self.style.SUCCESS('Successfully fetched RSS feeds'))