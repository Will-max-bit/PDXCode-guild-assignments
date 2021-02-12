from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    code = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.url
    