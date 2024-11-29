from django.shortcuts import render
from .models import FeedItem
from django.db.models import Sum

def home_view(request):
    feed_items = FeedItem.objects.order_by('-published_date')[:50]
    cards = feed_items[::1]
    rows = organize_cards(cards)
    card_sequence = [item for row in rows for item in row]
    return render(request, 'home.html', {'feed_items': card_sequence})

def widths_sum(cards):
    return sum(item.card_column_width for item in cards)

def fill_row(cards, n=0):
    if len(cards) == n or widths_sum(cards[0:n+1]) > 12:
        return cards[0:n]
    else:
        return fill_row(cards, n + 1)

def organize_cards(cards):
    rows = []
    while cards:
        current_row = fill_row(cards)
        for gap in [4, 3, 2]:
            if 12 - widths_sum(current_row) == gap and gap in cards:
                index = cards.index(gap)
                filler_card = cards.pop(index)
                current_row.append(filler_card)
        rows.append(current_row)
        cards = cards[len(current_row):]
    return rows

