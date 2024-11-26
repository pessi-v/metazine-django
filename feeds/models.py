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

    def __str__(self):
        return self.title