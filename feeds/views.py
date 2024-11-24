from django.shortcuts import render
from .models import FeedItem
import inflect

def home_view(request):
    i = inflect.engine()

    feed_items = FeedItem.objects.order_by('-published_date')[:50]
    feed_items_with_index_string = [(i.number_to_words(index), item) for index, item in enumerate(feed_items, start = 1)]
    return render(request, 'home.html', {'feed_items': feed_items_with_index_string})