from django.db import models

class RSSFeed(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    last_fetched = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class FeedItem(models.Model):
    feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=500)
    link = models.URLField()
    description = models.TextField()
    published_date = models.DateTimeField()
    unique_id = models.CharField(max_length=500, unique=True)
    og_image = models.URLField(null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    card_column_width = models.IntegerField(default=2)

    def save(self, *args, **kwargs):
        # Calculate card_column_width based on description length
        desc_length = len(self.title or '')
        if desc_length < 30:
            self.card_column_width = 2
        elif desc_length < 58:
            self.card_column_width = 3
        else:
            self.card_column_width = 4
        
        super().save(*args, **kwargs)
    
    @property
    def column_width(self):
        return self.card_column_width

    def __str__(self):
        return self.title