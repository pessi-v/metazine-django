from django.shortcuts import render
from .models import FeedItem

def home_view(request):
    feed_items = FeedItem.objects.order_by('-published_date')[:50]
    return render(request, 'home.html', {'feed_items': feed_items})