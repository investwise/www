from django.db import models
from django.utils import timezone

# Create your models here.
class NewsItem(models.Model):
    url = models.URLField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField()


    #def getURL(self):
    #    return self.url

    def __str__(self):
        return self.title

'''
class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
